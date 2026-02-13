"""
Dashboard Service for ISS Module v2.0
=====================================

Provides monitoring and record management for DALS, GOAT, True Mark NFT Mint,
and NFT records with internal serial number references.
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from pathlib import Path

from .models import (
    DALSRecord, GOATRecord, TrueMarkNFTMint, NFTRecord,
    DashboardSummary, SystemStatus, DashboardData
)
from .immutable_spice_layer import ImmutableSPICELayer


class DashboardService:
    """Service for dashboard operations and system monitoring"""

    def __init__(self, data_dir: str = "data/dashboard"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

        # Data files
        self.dals_file = self.data_dir / "dals_records.jsonl"
        self.goat_file = self.data_dir / "goat_records.jsonl"
        self.nft_mint_file = self.data_dir / "truemark_nft_mints.jsonl"
        self.nft_records_file = self.data_dir / "nft_records.jsonl"
        self.alerts_file = self.data_dir / "system_alerts.jsonl"

        # Initialize files if they don't exist
        for file_path in [self.dals_file, self.goat_file, self.nft_mint_file,
                         self.nft_records_file, self.alerts_file]:
            if not file_path.exists():
                file_path.touch()

        # SPICE layer for tamper-evident logging
        self.spice_layer = ImmutableSPICELayer()

    def _append_record(self, file_path: Path, record: Dict[str, Any]) -> str:
        """Append a record to a JSONL file with tamper-evident logging"""
        record_id = hashlib.sha256(
            f"{datetime.now().isoformat()}{json.dumps(record, sort_keys=True)}".encode()
        ).hexdigest()[:16]

        record_entry = {
            "record_id": record_id,
            "timestamp": datetime.now().isoformat(),
            "data": record
        }

        with open(file_path, 'a') as f:
            f.write(json.dumps(record_entry) + '\n')

        # Log to SPICE layer for tamper-evident audit trail
        descriptor = self.spice_layer.create_descriptor(
            process_name=f"dashboard_record_{file_path.stem}",
            process_version="1.0",
            capability_level=3,
            process_outcome="compliant",
            compliance_score=1.0,
            apriori_refs=[],
            aposteriori_refs=[record_id],
            glyph_range_start=record_id,
            glyph_range_end=record_id,
            glyph_count=1,
            evidence_required=["record_creation"],
            evidence_provided=["jsonl_append", "spice_logging"],
            assessed_by="dashboard_service",
            assessment_method="automated",
            active_constraints=[]
        )

        return record_id

    def _read_records(self, file_path: Path, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Read records from a JSONL file"""
        records = []
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    if line.strip():
                        records.append(json.loads(line))
                        if limit and len(records) >= limit:
                            break
        except FileNotFoundError:
            pass
        return records

    # DALS Operations
    def create_dals_record(self, record: DALSRecord) -> str:
        """Create a new DALS record"""
        return self._append_record(self.dals_file, record.dict())

    def get_dals_records(self, limit: Optional[int] = None) -> List[DALSRecord]:
        """Get DALS records"""
        records = self._read_records(self.dals_file, limit)
        return [DALSRecord(**record["data"]) for record in records]

    # GOAT Operations
    def create_goat_record(self, record: GOATRecord) -> str:
        """Create a new GOAT record"""
        return self._append_record(self.goat_file, record.dict())

    def get_goat_records(self, limit: Optional[int] = None) -> List[GOATRecord]:
        """Get GOAT records"""
        records = self._read_records(self.goat_file, limit)
        return [GOATRecord(**record["data"]) for record in records]

    def update_goat_status(self, record_id: str, status: str, result: Optional[Dict] = None) -> bool:
        """Update GOAT record status"""
        # This would require more complex logic to update existing records
        # For now, we'll create a new record with updated status
        update_record = {
            "operation_type": "status_update",
            "original_record_id": record_id,
            "new_status": status,
            "result": result or {},
            "updated_at": datetime.now().isoformat()
        }
        self._append_record(self.goat_file, update_record)
        return True

    # True Mark NFT Mint Operations
    def create_nft_mint(self, mint: TrueMarkNFTMint) -> str:
        """Create a new NFT mint record"""
        return self._append_record(self.nft_mint_file, mint.dict())

    def get_nft_mints(self, limit: Optional[int] = None) -> List[TrueMarkNFTMint]:
        """Get NFT mint records"""
        records = self._read_records(self.nft_mint_file, limit)
        return [TrueMarkNFTMint(**record["data"]) for record in records]

    # NFT Records Operations
    def create_nft_record(self, record: NFTRecord) -> str:
        """Create a new NFT record with internal serial numbers"""
        return self._append_record(self.nft_records_file, record.dict())

    def get_nft_records(self, limit: Optional[int] = None) -> List[NFTRecord]:
        """Get NFT records"""
        records = self._read_records(self.nft_records_file, limit)
        return [NFTRecord(**record["data"]) for record in records]

    def find_nft_by_serial(self, serial_number: str) -> List[NFTRecord]:
        """Find NFT records by DALS or TrueMark serial number"""
        all_records = self.get_nft_records()
        matching = []
        for record in all_records:
            if (serial_number in record.dals_serial_numbers or
                serial_number in record.truemark_serial_numbers):
                matching.append(record)
        return matching

    # Dashboard Operations
    def get_dashboard_summary(self) -> DashboardSummary:
        """Get dashboard summary statistics"""
        dals_count = len(self.get_dals_records())
        goat_count = len(self.get_goat_records())
        nft_mint_count = len(self.get_nft_mints())
        nft_record_count = len(self.get_nft_records())

        # Count active GOAT operations
        goat_records = self.get_goat_records()
        active_ops = sum(1 for r in goat_records if r.status in ["pending", "running"])

        # System health based on recent activity
        health = "healthy"
        if active_ops > 10:  # Arbitrary threshold
            health = "warning"
        if active_ops > 20:
            health = "error"

        return DashboardSummary(
            total_dals_records=dals_count,
            total_goat_records=goat_count,
            total_nft_mints=nft_mint_count,
            total_nft_records=nft_record_count,
            active_operations=active_ops,
            system_health=health,
            last_updated=datetime.now().isoformat()
        )

    def get_system_statuses(self) -> List[SystemStatus]:
        """Get status for each monitored system"""
        statuses = []

        # DALS Status
        dals_records = self._read_records(self.dals_file, limit=1)
        last_dals = dals_records[0]["timestamp"] if dals_records else None
        statuses.append(SystemStatus(
            system_name="DALS",
            status="healthy",
            record_count=len(self.get_dals_records()),
            last_activity=last_dals or "never",
            uptime_percentage=99.9,  # Mock value
            alerts=[]
        ))

        # GOAT Status
        goat_records = self._read_records(self.goat_file, limit=1)
        last_goat = goat_records[0]["timestamp"] if goat_records else None
        active_goat = len([r for r in self.get_goat_records() if r.status in ["pending", "running"]])
        goat_alerts = []
        if active_goat > 5:
            goat_alerts.append("High number of active operations")
        statuses.append(SystemStatus(
            system_name="GOAT",
            status="warning" if active_goat > 5 else "healthy",
            record_count=len(self.get_goat_records()),
            last_activity=last_goat or "never",
            uptime_percentage=98.5,  # Mock value
            alerts=goat_alerts
        ))

        # True Mark NFT Status
        nft_records = self._read_records(self.nft_mint_file, limit=1)
        last_nft = nft_records[0]["timestamp"] if nft_records else None
        statuses.append(SystemStatus(
            system_name="True Mark NFT",
            status="healthy",
            record_count=len(self.get_nft_mints()),
            last_activity=last_nft or "never",
            uptime_percentage=99.5,  # Mock value
            alerts=[]
        ))

        # NFT Records Status
        nft_rec_records = self._read_records(self.nft_records_file, limit=1)
        last_nft_rec = nft_rec_records[0]["timestamp"] if nft_rec_records else None
        statuses.append(SystemStatus(
            system_name="NFT Records",
            status="healthy",
            record_count=len(self.get_nft_records()),
            last_activity=last_nft_rec or "never",
            uptime_percentage=99.7,  # Mock value
            alerts=[]
        ))

        return statuses

    def get_recent_activities(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent activities across all systems"""
        activities = []

        # Collect recent records from all systems
        for system_name, file_path in [
            ("DALS", self.dals_file),
            ("GOAT", self.goat_file),
            ("True Mark NFT", self.nft_mint_file),
            ("NFT Records", self.nft_records_file)
        ]:
            records = self._read_records(file_path, limit=limit)
            for record in records:
                activities.append({
                    "system": system_name,
                    "timestamp": record["timestamp"],
                    "record_id": record["record_id"],
                    "type": "record_created"
                })

        # Sort by timestamp and return most recent
        activities.sort(key=lambda x: x["timestamp"], reverse=True)
        return activities[:limit]

    def get_dashboard_data(self) -> DashboardData:
        """Get complete dashboard data"""
        return DashboardData(
            summary=self.get_dashboard_summary(),
            system_statuses=self.get_system_statuses(),
            recent_activities=self.get_recent_activities(),
            alerts=[]  # Could be populated from alerts file
        )

    def create_alert(self, alert_type: str, message: str, severity: str = "info") -> str:
        """Create a system alert"""
        alert = {
            "alert_type": alert_type,
            "message": message,
            "severity": severity,
            "created_at": datetime.now().isoformat()
        }
        return self._append_record(self.alerts_file, alert)