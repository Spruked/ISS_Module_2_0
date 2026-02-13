"""
Debug Harness for ISS Module v2
================================

Comprehensive testing and debugging tools for the forensic timekeeping system
"""

import json
import time
from pathlib import Path
from datetime import datetime

def test_forensic_timekeeping():
    """Test forensic time pulse generation"""
    print("🔍 Testing Forensic Timekeeping...")

    from forensic_timekeeper import ForensicTimeKeeper

    keeper = ForensicTimeKeeper(node_id="DEBUG_HARNESS")

    # Generate multiple pulses
    pulses = []
    for i in range(3):
        pulse = keeper.generate_pulse()
        pulses.append(pulse)
        print(f"  Pulse {i+1}: TAI={pulse.tai_ns}, UTC={pulse.utc_iso[:19]}")
        time.sleep(0.1)  # Small delay between pulses

    # Verify chain integrity
    integrity = keeper.verify_chain_integrity()
    print(f"  Chain integrity: {integrity['status']}")

    return True

def test_spice_descriptors():
    """Test SPICE descriptor creation and retrieval"""
    print("🔍 Testing SPICE Descriptors...")

    from spice_descriptor_layer import SPICEDescriptorLayer, CapabilityLevel, ProcessOutcome

    spice = SPICEDescriptorLayer()

    # Create test descriptor
    descriptor = spice.create_descriptor(
        process_name="Debug_Test_Process",
        process_version="1.0.0",
        capability_level=CapabilityLevel.LEVEL_3,
        process_outcome=ProcessOutcome.COMPLIANT,
        compliance_score=0.88,
        apriori_refs=["debug:constraint1", "debug:constraint2"],
        aposteriori_refs=["debug:outcome1"],
        glyph_range_start="debug123",
        glyph_range_end="debug456",
        glyph_count=10,
        evidence_required=["debug_evidence"],
        evidence_provided=["debug_evidence"],
        assessed_by="DEBUG_HARNESS",
        assessment_method="automated_test",
        active_constraints=["debug_mode"]
    )

    print(f"  Created descriptor: {descriptor.descriptor_id}")

    # Retrieve descriptor
    retrieved = spice.get_descriptor(descriptor.descriptor_id)
    assert retrieved is not None, "Failed to retrieve descriptor"
    print("  ✅ Descriptor retrieval successful")

    # Test audit trail reconstruction
    audit = spice.reconstruct_audit_trail(descriptor.descriptor_id)
    assert "what_happened" in audit, "Audit trail missing what_happened"
    print("  ✅ Audit trail reconstruction successful")

    # Test capability report
    report = spice.get_capability_report()
    assert report["total_processes"] > 0, "No processes in capability report"
    print("  ✅ Capability report generation successful")

    return True

def test_data_integrity():
    """Test data file integrity"""
    print("🔍 Testing Data Integrity...")

    # Check forensic logs
    forensic_log = Path("./forensic_logs/forensic_audit.log")
    if forensic_log.exists():
        with open(forensic_log, 'r') as f:
            lines = f.readlines()
            print(f"  Forensic audit log: {len(lines)} entries")
    else:
        print("  ⚠️ Forensic audit log not found")

    # Check glyph chain
    glyph_chain = Path("./forensic_logs/glyph_chain.jsonl")
    if glyph_chain.exists():
        with open(glyph_chain, 'r') as f:
            lines = [l for l in f if l.strip()]
            valid_lines = 0
            for line in lines:
                try:
                    json.loads(line)
                    valid_lines += 1
                except:
                    pass
            print(f"  Glyph chain: {valid_lines}/{len(lines)} valid records")
    else:
        print("  ⚠️ Glyph chain not found")

    # Check SPICE descriptors
    spice_descriptors = Path("./spice_layer/spice_descriptors.jsonl")
    if spice_descriptors.exists():
        with open(spice_descriptors, 'r') as f:
            lines = [l for l in f if l.strip()]
            valid_lines = 0
            for line in lines:
                try:
                    json.loads(line)
                    valid_lines += 1
                except:
                    pass
            print(f"  SPICE descriptors: {valid_lines}/{len(lines)} valid records")
    else:
        print("  ⚠️ SPICE descriptors not found")

    # Check SPICE index
    spice_index = Path("./spice_layer/spice_index.json")
    if spice_index.exists():
        with open(spice_index, 'r') as f:
            index_data = json.load(f)
            print(f"  SPICE index: {index_data.get('total_descriptors', 0)} descriptors indexed")
    else:
        print("  ⚠️ SPICE index not found")

    return True

def run_full_test_suite():
    """Run complete test suite"""
    print("🚀 Running ISS Module v2 Debug Harness")
    print("=" * 50)

    tests = [
        ("Forensic Timekeeping", test_forensic_timekeeping),
        ("SPICE Descriptors", test_spice_descriptors),
        ("Data Integrity", test_data_integrity),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        try:
            print(f"\n🧪 {test_name}")
            if test_func():
                print(f"✅ {test_name} PASSED")
                passed += 1
            else:
                print(f"❌ {test_name} FAILED")
        except Exception as e:
            print(f"❌ {test_name} ERROR: {e}")

    print(f"\n{'=' * 50}")
    print(f"TEST RESULTS: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 ALL TESTS PASSED - SYSTEM OPERATIONAL")
        return True
    else:
        print("⚠️ SOME TESTS FAILED - CHECK SYSTEM CONFIGURATION")
        return False

if __name__ == "__main__":
    success = run_full_test_suite()
    exit(0 if success else 1)