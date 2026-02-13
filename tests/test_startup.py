#!/usr/bin/env python3
"""
ISS Module v2 - Startup Test
===========================

Test script to validate FastAPI implementation
"""

import sys
import os
sys.path.append('.')

def test_imports():
    """Test all imports work correctly"""
    try:
        from main import app
        print("✅ FastAPI app imported successfully")

        from forensic_time_plugin import ForensicTimePlugin
        print("✅ ForensicTimePlugin imported successfully")

        from spice_descriptor_layer import SPICEDescriptorLayer
        print("✅ SPICEDescriptorLayer imported successfully")

        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_basic_functionality():
    """Test basic functionality"""
    try:
        from fastapi.testclient import TestClient
        from main import app

        client = TestClient(app)

        # Test health check
        response = client.get('/health')
        if response.status_code == 200:
            data = response.json()
            print("✅ Health check endpoint working")
            print(f"   Status: {data.get('status')}")
            print(f"   Forensic integrity: {data.get('forensic_chain_integrity')}")
            print(f"   SPICE integrity: {data.get('spice_layer_integrity')}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False

        # Test time pulse
        response = client.get('/time/pulse')
        if response.status_code == 200:
            data = response.json()
            print("✅ Time pulse endpoint working")
            print(f"   Has TAI: {'tai_ns' in data}")
            print(f"   Has UTC: {'utc_iso' in data}")
            print(f"   Has glyph_hash: {'glyph_hash' in data}")
        else:
            print(f"❌ Time pulse failed: {response.status_code}")
            return False

        return True
    except Exception as e:
        print(f"❌ Functionality test error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🔍 ISS Module v2 - Startup Test")
    print("=" * 40)

    success = True

    print("\n📦 Testing imports...")
    if not test_imports():
        success = False

    print("\n⚙️  Testing basic functionality...")
    if not test_basic_functionality():
        success = False

    print("\n" + "=" * 40)
    if success:
        print("🎉 ISS Module v2 FastAPI implementation is READY!")
        print("\n🚀 To start the server:")
        print("   python main.py")
        print("   # or")
        print("   docker-compose up")
        print("\n📋 API Documentation: http://localhost:8000/docs")
    else:
        print("❌ ISS Module v2 has issues that need to be resolved")
        sys.exit(1)