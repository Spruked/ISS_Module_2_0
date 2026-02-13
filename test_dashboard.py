#!/usr/bin/env python3
"""
Test Dashboard API Endpoints
============================
"""

import requests
import json

def test_dashboard_endpoints():
    """Test dashboard API endpoints"""

    base_url = "http://localhost:8001"

    print("🔍 Testing Dashboard API Endpoints...")

    # Test dashboard summary
    try:
        response = requests.get(f"{base_url}/dashboard/summary")
        if response.status_code == 200:
            data = response.json()
            print("✅ Dashboard summary endpoint working")
            print(f"   Total DALS records: {data['total_dals_records']}")
            print(f"   Total GOAT records: {data['total_goat_records']}")
            print(f"   Total NFT records: {data['total_nft_records']}")
        else:
            print(f"❌ Dashboard summary failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Could not connect to dashboard summary: {e}")

    # Test NFT serial search
    try:
        response = requests.get(f"{base_url}/dashboard/nft/find/TM-2024-001")
        if response.status_code == 200:
            data = response.json()
            print("✅ NFT serial search working")
            print(f"   Found {len(data)} NFT(s) with serial TM-2024-001")
        else:
            print(f"❌ NFT serial search failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Could not connect to NFT search: {e}")

    # Test dashboard data
    try:
        response = requests.get(f"{base_url}/dashboard/data")
        if response.status_code == 200:
            data = response.json()
            print("✅ Complete dashboard data endpoint working")
            print(f"   System health: {data['summary']['system_health']}")
            print(f"   Active operations: {data['summary']['active_operations']}")
        else:
            print(f"❌ Dashboard data failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Could not connect to dashboard data: {e}")

if __name__ == "__main__":
    test_dashboard_endpoints()