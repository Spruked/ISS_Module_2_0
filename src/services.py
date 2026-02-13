"""
ISS MODULE V2 - Service Layer
=============================

Service classes for forensic timekeeping and SPICE descriptor management
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .forensic_timekeeper import ForensicTimeKeeper, StarDatePulse
from .spice_descriptor_layer import SPICEDescriptorLayer, SPICEDescriptor, ProcessOutcome, CapabilityLevel

class ForensicService:
    """Service for forensic timekeeping operations"""

    def __init__(self):
        self.service = ForensicTimeKeeper(
            node_id="ISS_MODULE_V2",
            storage_path="./forensic_logs"
        )

    def generate_pulse(self) -> StarDatePulse:
        """Generate new forensic time pulse"""
        return self.service.generate_pulse()

    def verify_chain_integrity(self) -> Dict[str, Any]:
        """Verify glyph chain integrity"""
        return self.service.verify_chain_integrity()

    def get_pulse_history(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get pulse history"""
        return self.service.get_pulse_history(limit)

class SPICEService:
    """Service for SPICE descriptor operations"""

    def __init__(self):
        self.service = SPICEDescriptorLayer()

    def create_descriptor(self, data) -> SPICEDescriptor:
        """Create new SPICE descriptor"""
        # Convert string outcome to enum
        outcome_enum = ProcessOutcome(data.process_outcome.lower())

        return self.service.create_descriptor(
            process_name=data.process_name,
            process_version=data.process_version,
            capability_level=CapabilityLevel(data.capability_level),
            process_outcome=outcome_enum,
            compliance_score=data.compliance_score,
            apriori_refs=data.apriori_refs,
            aposteriori_refs=data.aposteriori_refs,
            glyph_range_start=data.glyph_range_start,
            glyph_range_end=data.glyph_range_end,
            glyph_count=data.glyph_count,
            evidence_required=data.evidence_required,
            evidence_provided=data.evidence_provided,
            assessed_by=data.assessed_by,
            assessment_method=data.assessment_method,
            active_constraints=data.active_constraints
        )

    def get_descriptor(self, descriptor_id: str) -> Optional[SPICEDescriptor]:
        """Get SPICE descriptor by ID"""
        return self.service.get_descriptor(descriptor_id)

    def find_by_glyph(self, glyph_hash: str) -> List[SPICEDescriptor]:
        """Find descriptors referencing specific glyph"""
        return self.service.find_by_glyph(glyph_hash)

    def find_by_apriori(self, apriori_id: str) -> List[SPICEDescriptor]:
        """Find descriptors referencing apriori entry"""
        return self.service.find_by_apriori_ref(apriori_id)

    def reconstruct_audit_trail(self, descriptor_id: str) -> Dict[str, Any]:
        """Full audit trail reconstruction"""
        return self.service.reconstruct_audit_trail(descriptor_id)

    def get_capability_report(self) -> Dict[str, Any]:
        """Get process maturity report"""
        return self.service.get_capability_report()

    def verify_integrity(self) -> bool:
        """Verify SPICE layer integrity"""
        try:
            # Check if index file exists and is valid
            if not self.service.index_file.exists():
                return False

            # Check if descriptor file exists
            if not self.service.descriptor_file.exists():
                return False

            # Basic integrity checks
            report = self.get_capability_report()
            return report.get("total_processes", 0) >= 0
        except Exception:
            return False