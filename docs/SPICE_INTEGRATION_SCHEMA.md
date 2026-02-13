# SPICE DESCRIPTOR LAYER - INTEGRATION SCHEMA
# =============================================
#
# Architecture: Non-cognitive, referential, advisory only
# Constitutional Article VII: All memory is immutable and auditable
#

## 1. DIRECTORY STRUCTURE

```
memory_matrix/
├── apriori_vault.jsonl          # Immutable truths (untouched)
├── aposteriori_vault.jsonl      # Validated learning (untouched)
├── trace_vault.jsonl            # Glyph chain (untouched)
├── ghost_layer/                 # Decaying semantic wakes
└── spice_layer/                 # NEW: Process metadata layer
    ├── spice_descriptors.jsonl  # Immutable descriptor chain
    ├── spice_index.json         # Fast lookup index
    ├── constitutional_binding.jsonl
    └── process_definitions/     # Process type schemas
        ├── WorkerSKG.json
        ├── CALI_Cognition.json
        └── DALS_Execution.json
```

## 2. SPICE DESCRIPTOR SCHEMA

```json
{
  "descriptor_id": "sha256:16chars",
  "process_name": "WorkerSKG_Job_Execution",
  "process_version": "2.1.0",

  "capability_level": 4,
  "process_outcome": "compliant",
  "compliance_score": 0.94,

  "vault_refs": {
    "apriori": ["apriori:deterministic_replay", "apriori:glyph_logging"],
    "aposteriori": ["aposteriori:job_success_rate"]
  },

  "trace_refs": {
    "glyph_range_start": "a1b2c3d4...",
    "glyph_range_end": "e5f6g7h8...",
    "glyph_count": 42,
    "forensic_time_start": "2026-02-13T05:00:00Z",
    "forensic_time_end": "2026-02-13T05:00:42Z"
  },

  "evidence": {
    "required": ["job_input", "job_output", "execution_log"],
    "provided": ["job_input", "job_output", "execution_log", "forensic_timestamp"],
    "gaps": []
  },

  "assessment": {
    "assessed_by": "CALI_AUDIT_MODULE",
    "assessed_at": "2026-02-13T05:01:00Z",
    "method": "deterministic_replay_verification",
    "validator": "SPICE_ASSESSMENT_SKG"
  },

  "constraints_active": [
    "immutable_memory",
    "constitutional_article_vii",
    "deterministic_replay"
  ],

  "advisory": {
    "notes": "Level 4 capability demonstrated",
    "confidence": 0.94,
    "authority": "NON_AUTHORITATIVE"
  }
}
```

## 3. INTEGRATION RULES (CRITICAL)

### Rule 1: NEVER Write to Vaults
- SPICE layer ONLY reads from apriori/aposteriori/trace vaults
- NEVER writes to vault files
- NEVER modifies vault contents
- NEVER stores SPICE data inside vaults

### Rule 2: Reference Only
- All vault interactions are pointers/references
- Use descriptor IDs, not content
- Use glyph hashes, not glyph data
- Use vault entry IDs, not vault entries

### Rule 3: Non-Authoritative
- SPICE descriptors are advisory only
- Cannot override vault decisions
- Cannot modify cognitive processes
- Cannot elevate capability levels by convenience

### Rule 4: Immutable Append-Only
- Descriptors are written once, never modified
- Index is regenerated, never edited in place
- Violations trigger constitutional alerts

## 4. ISS MODULE V2 INTEGRATION

### FastAPI Endpoints

```python
from fastapi import FastAPI
from spice_descriptor_layer import SPICEDescriptorLayer, CapabilityLevel

app = FastAPI()
spice = SPICEDescriptorLayer()

@app.post("/spice/descriptor")
async def create_descriptor(process_data: ProcessData):
    """Create new SPICE descriptor"""
    descriptor = spice.create_descriptor(
        process_name=process_data.name,
        capability_level=CapabilityLevel(process_data.level),
        # ... other params
    )
    return {"descriptor_id": descriptor.descriptor_id}

@app.get("/spice/audit/{descriptor_id}")
async def get_audit_trail(descriptor_id: str):
    """Full audit trail reconstruction"""
    return spice.reconstruct_audit_trail(descriptor_id)

@app.get("/spice/find/glyph/{glyph_hash}")
async def find_by_glyph(glyph_hash: str):
    """Find descriptors by glyph reference"""
    descriptors = spice.find_by_glyph(glyph_hash)
    return {"descriptors": [d.to_dict() for d in descriptors]}

@app.get("/spice/capability/report")
async def capability_report():
    """Process maturity report"""
    return spice.get_capability_report()

@app.get("/spice/verify/integrity")
async def verify_spice_integrity():
    """Verify SPICE layer integrity"""
    # Check index consistency
    # Check descriptor chain continuity
    # Verify no vault contamination
    pass
```

## 5. WORKER SKG INTEGRATION

```python
class SPICEAwareWorker:
    def __init__(self):
        self.spice = SPICEDescriptorLayer()
        self.forensic_time = ForensicTimePlugin()
    
    def execute_job(self, job):
        # Start forensic timestamp
        start_pulse = self.forensic_time.pulse()
        
        # Execute job
        result = self._process_job(job)
        
        # End forensic timestamp
        end_pulse = self.forensic_time.pulse()
        
        # Create SPICE descriptor
        descriptor = self.spice.create_descriptor(
            process_name="WorkerSKG_Job_Execution",
            capability_level=CapabilityLevel.LEVEL_4,
            process_outcome=ProcessOutcome.COMPLIANT if result.success else ProcessOutcome.NON_COMPLIANT,
            glyph_range_start=start_pulse['glyph_hash'],
            glyph_range_end=end_pulse['glyph_hash'],
            # ... other metadata
        )
        
        return {
            "result": result,
            "spice_descriptor_id": descriptor.descriptor_id,
            "audit_trail": self.spice.reconstruct_audit_trail(descriptor.descriptor_id)
        }
```

## 6. CALI ORB INTEGRATION

```python
class CALISPICEBridge:
    """CALI ORB integration with SPICE layer"""
    
    def __init__(self):
        self.spice = SPICEDescriptorLayer()
        self.cali_matrix = CALIMemoryMatrix()
    
    def log_cognitive_event(self, thought_data, process_result):
        """Log cognitive event with SPICE metadata"""
        
        # Get glyph range from forensic time
        glyph_start = process_result['start_glyph']
        glyph_end = process_result['end_glyph']
        
        # Create SPICE descriptor for cognitive process
        descriptor = self.spice.create_descriptor(
            process_name="CALI_Cognitive_Processing",
            process_version="2.1.0",
            capability_level=CapabilityLevel.LEVEL_5,  # Innovating
            apriori_refs=["apriori:reflection_loops", "apriori:confidence_capping"],
            aposteriori_refs=["aposteriori:pattern_recognition"],
            glyph_range_start=glyph_start,
            glyph_range_end=glyph_end,
            active_constraints=["confidence_cap_0.75", "tension_ledger"],
            assessed_by="CALI_SELF_AUDIT"
        )
        
        # Append to CALI immutable matrix
        self.cali_matrix.append({
            "thought": thought_data,
            "spice_descriptor_id": descriptor.descriptor_id,
            "constitutional_compliance": "VERIFIED"
        })
```

## 7. TRACEABILITY ACCELERATOR

The SPICE layer provides O(1) lookups for:

- **What happened**: Process name, version, outcome
- **Why it happened**: Apriori constraints, active rules
- **How it happened**: Capability level, assessment method
- **What was learned**: Aposteriori references
- **Where to find it**: Glyph range, vault pointers

Instead of scanning entire vaults, auditors:
1. Get SPICE descriptor (O(1) via index)
2. Follow vault pointers to relevant entries
3. Reconstruct full context in milliseconds

## 8. COMPLIANCE SCORING

```python
def calculate_compliance_score(descriptor: SPICEDescriptor) -> float:
    """
    Calculate compliance score based on:
    - Evidence completeness (required vs provided)
    - Capability level achieved
    - Constraint adherence
    - Audit trail completeness
    """
    evidence_score = len(descriptor.evidence_provided) / len(descriptor.evidence_required)
    capability_score = descriptor.capability_level.value / 5.0
    constraint_score = 1.0 if len(descriptor.active_constraints) > 0 else 0.0
    
    return (evidence_score * 0.4 + capability_score * 0.4 + constraint_score * 0.2)
```

## 9. CONSTITUTIONAL SAFEGUARDS

```python
class ConstitutionalEnforcer:
    """Prevents SPICE layer from contaminating vaults"""
    
    def verify_no_vault_contamination(self):
        """Verify SPICE layer never wrote to vault files"""
        # Check file modification times
        # Verify vault hashes unchanged
        # Alert if contamination detected
        pass
    
    def verify_non_authoritative(self, descriptor: SPICEDescriptor):
        """Verify descriptor is advisory only"""
        assert descriptor.advisory["authority"] == "NON_AUTHORITATIVE"
        assert "OVERRIDE" not in descriptor.advisory["notes"].upper()
```