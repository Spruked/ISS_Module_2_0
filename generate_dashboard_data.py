#!/usr/bin/env python3
"""
Dashboard Test Data Generator
=============================

Generates sample data for testing the ISS Module v2.0 dashboard
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dashboard_service import DashboardService
from src.models import DALSRecord, GOATRecord, TrueMarkNFTMint, NFTRecord
from datetime import datetime
import json

def generate_sample_data():
    """Generate sample data for dashboard testing"""

    dashboard = DashboardService()

    print("🔄 Generating sample dashboard data...")

    # Sample DALS Records
    dals_records = [
        DALSRecord(
            record_id="",
            asset_type="digital_artwork",
            asset_hash="a1b2c3d4e5f6...",
            owner_id="user_001",
            transfer_history=[
                {"from": "creator", "to": "user_001", "timestamp": "2024-01-01T10:00:00Z"}
            ],
            metadata={"title": "Digital Masterpiece", "artist": "Artist One"},
            created_at=datetime.now().isoformat(),
            last_updated=datetime.now().isoformat()
        ),
        DALSRecord(
            record_id="",
            asset_type="music_track",
            asset_hash="f6e5d4c3b2a1...",
            owner_id="user_002",
            transfer_history=[
                {"from": "creator", "to": "user_002", "timestamp": "2024-01-02T14:30:00Z"}
            ],
            metadata={"title": "Epic Symphony", "artist": "Composer Two"},
            created_at=datetime.now().isoformat(),
            last_updated=datetime.now().isoformat()
        )
    ]

    for record in dals_records:
        record_id = dashboard.create_dals_record(record)
        print(f"✅ Created DALS record: {record_id}")

    # Sample GOAT Records
    goat_records = [
        GOATRecord(
            record_id="",
            operation_type="data_processing",
            status="completed",
            parameters={"input_size": 1024, "algorithm": "fft"},
            result={"output_size": 512, "processing_time": 2.5},
            execution_time=2.5,
            created_at=datetime.now().isoformat(),
            completed_at=datetime.now().isoformat()
        ),
        GOATRecord(
            record_id="",
            operation_type="image_analysis",
            status="running",
            parameters={"image_url": "https://example.com/image.jpg", "model": "resnet50"},
            result=None,
            execution_time=None,
            created_at=datetime.now().isoformat(),
            completed_at=None
        ),
        GOATRecord(
            record_id="",
            operation_type="text_processing",
            status="pending",
            parameters={"text_length": 5000, "language": "en"},
            result=None,
            execution_time=None,
            created_at=datetime.now().isoformat(),
            completed_at=None
        )
    ]

    for record in goat_records:
        record_id = dashboard.create_goat_record(record)
        print(f"✅ Created GOAT record: {record_id}")

    # Sample True Mark NFT Mints
    nft_mints = [
        TrueMarkNFTMint(
            mint_id="",
            nft_contract="0x1234567890123456789012345678901234567890",
            token_id="1",
            serial_number="TM-2024-001",
            metadata_uri="ipfs://QmExample123...",
            minter_address="0xabcdef1234567890abcdef1234567890abcdef12",
            royalty_percentage=5.0,
            attributes={"rarity": "legendary", "edition": "1/1"},
            created_at=datetime.now().isoformat()
        ),
        TrueMarkNFTMint(
            mint_id="",
            nft_contract="0x1234567890123456789012345678901234567890",
            token_id="2",
            serial_number="TM-2024-002",
            metadata_uri="ipfs://QmExample456...",
            minter_address="0xabcdef1234567890abcdef1234567890abcdef12",
            royalty_percentage=2.5,
            attributes={"rarity": "rare", "edition": "50/100"},
            created_at=datetime.now().isoformat()
        )
    ]

    for mint in nft_mints:
        mint_id = dashboard.create_nft_mint(mint)
        print(f"✅ Created NFT mint: {mint_id}")

    # Sample NFT Records with internal serial numbers
    nft_records = [
        NFTRecord(
            record_id="",
            nft_info=nft_mints[0],
            dals_serial_numbers=["DALS-ART-001", "DALS-ART-002"],
            truemark_serial_numbers=["TM-2024-001"],
            ownership_chain=[
                {"owner": "minter", "timestamp": "2024-01-01T10:00:00Z"},
                {"owner": "user_001", "timestamp": "2024-01-02T15:30:00Z"}
            ],
            verification_status="verified",
            last_verified=datetime.now().isoformat(),
            metadata={"collection": "Digital Art Masters", "license": "CC BY-SA"}
        ),
        NFTRecord(
            record_id="",
            nft_info=nft_mints[1],
            dals_serial_numbers=["DALS-MUSIC-001"],
            truemark_serial_numbers=["TM-2024-002", "TM-2024-003"],
            ownership_chain=[
                {"owner": "minter", "timestamp": "2024-01-03T09:15:00Z"}
            ],
            verification_status="pending_verification",
            last_verified=datetime.now().isoformat(),
            metadata={"collection": "Music NFTs", "genre": "classical"}
        )
    ]

    for record in nft_records:
        record_id = dashboard.create_nft_record(record)
        print(f"✅ Created NFT record: {record_id}")

    print("\n🎉 Sample data generation complete!")
    print("📊 Dashboard should now show populated data")
    print("🔍 Try searching for serial numbers: TM-2024-001, DALS-ART-001, etc.")

if __name__ == "__main__":
    generate_sample_data()