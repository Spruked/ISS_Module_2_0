"""
Usage Examples for ISS Module v2
=================================

Practical examples of how to use the forensic timekeeping and SPICE descriptor system
"""

# Example 1: Basic Forensic Time Pulse Generation
print("=== Example 1: Forensic Time Pulse ===")
from forensic_timekeeper import ForensicTimeKeeper

keeper = ForensicTimeKeeper(node_id="EXAMPLE_NODE")
pulse = keeper.generate_pulse()
print(f"TAI: {pulse.tai_ns}")
print(f"UTC: {pulse.utc_iso}")
print(f"ET: {pulse.et_s}")
print()

# Example 2: SPICE Descriptor Creation
print("=== Example 2: SPICE Descriptor Creation ===")
from spice_descriptor_layer import SPICEDescriptorLayer, CapabilityLevel, ProcessOutcome

spice = SPICEDescriptorLayer()
descriptor = spice.create_descriptor(
    process_name="Example_Process",
    process_version="1.0.0",
    capability_level=CapabilityLevel.LEVEL_4,
    process_outcome=ProcessOutcome.COMPLIANT,
    compliance_score=0.95,
    apriori_refs=["constraint:time_accuracy", "constraint:data_integrity"],
    aposteriori_refs=["outcome:successful_execution", "outcome:performance_metrics"],
    glyph_range_start="abc123",
    glyph_range_end="xyz789",
    glyph_count=50,
    evidence_required=["input_validation", "output_verification"],
    evidence_provided=["input_validated", "output_verified", "audit_log"],
    assessed_by="EXAMPLE_ASSESSOR",
    assessment_method="automated_verification",
    active_constraints=["immutable_memory", "constitutional_compliance"]
)
print(f"Created descriptor: {descriptor.descriptor_id}")
print()

# Example 3: Audit Trail Reconstruction
print("=== Example 3: Audit Trail Reconstruction ===")
audit = spice.reconstruct_audit_trail(descriptor.descriptor_id)
print("What happened:", audit["what_happened"]["process"])
print("Why it happened:", len(audit["why_it_happened"]["apriori_constraints"]), "constraints")
print("How it happened:", audit["how_it_happened"]["capability_level"], "capability level")
print()

# Example 4: Capability Report
print("=== Example 4: Capability Report ===")
report = spice.get_capability_report()
print(f"Total processes: {report['total_processes']}")
print(f"Average capability: {report['average_capability']:.1f}")
print()

print("✅ All examples completed successfully!")