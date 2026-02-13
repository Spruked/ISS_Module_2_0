"""
SPICE DESCRIPTOR LAYER v1.0
=============================
Process-maturity metadata layer for Memory Matrix
Constitutional Article VII: All memory is immutable and auditable

Architecture:
- NON-COGNITIVE: Metadata only, never cognitive
- REFERENTIAL: Only pointers to vaults, never content
- NON-AUTHORITATIVE: Advisory only, cannot override decisions
- IMMUTABLE: Append-only JSONL format
- EXTERNAL: Separate directory from vaults
"""

import json
import hashlib
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from pathlib import Path
from enum import Enum


class CapabilityLevel(Enum):
    """SPICE capability levels 0-5"""
    LEVEL_0 = 0  # Incomplete
    LEVEL_1 = 1  # Performed
    LEVEL_2 = 2  # Managed
    LEVEL_3 = 3  # Established
    LEVEL_4 = 4  # Predictable
    LEVEL_5 = 5  # Innovating


class ProcessOutcome(Enum):
    """Process outcome classifications"""
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIAL = "partial"
    NOT_ASSESSED = "not_assessed"


@dataclass
class SPICEDescriptor:
    """
    SPICE process descriptor - NON-COGNITIVE metadata only
    """
    descriptor_id: str
    process_name: str
    process_version: str
    capability_level: int  # Store as int for JSON serialization
    process_outcome: str   # Store as str for JSON serialization
    compliance_score: float
    apriori_refs: List[str]
    aposteriori_refs: List[str]
    glyph_range_start: str
    glyph_range_end: str
    glyph_count: int
    evidence_required: List[str]
    evidence_provided: List[str]
    assessed_by: str
    assessed_at: str
    assessment_method: str
    active_constraints: List[str]
    advisory_notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'descriptor_id': self.descriptor_id,
            'process_name': self.process_name,
            'process_version': self.process_version,
            'capability_level': self.capability_level,
            'process_outcome': self.process_outcome,
            'compliance_score': self.compliance_score,
            'apriori_refs': self.apriori_refs,
            'aposteriori_refs': self.aposteriori_refs,
            'glyph_range_start': self.glyph_range_start,
            'glyph_range_end': self.glyph_range_end,
            'glyph_count': self.glyph_count,
            'evidence_required': self.evidence_required,
            'evidence_provided': self.evidence_provided,
            'assessed_by': self.assessed_by,
            'assessed_at': self.assessed_at,
            'assessment_method': self.assessment_method,
            'active_constraints': self.active_constraints,
            'advisory_notes': self.advisory_notes
        }
    
    def to_json(self) -> str:
        """Compact JSON for JSONL storage"""
        return json.dumps(self.to_dict(), separators=(',', ':'))
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SPICEDescriptor':
        """Create SPICEDescriptor from dictionary"""
        return cls(
            descriptor_id=data['descriptor_id'],
            process_name=data['process_name'],
            process_version=data['process_version'],
            capability_level=data['capability_level'],
            process_outcome=data['process_outcome'],
            compliance_score=data['compliance_score'],
            apriori_refs=data['apriori_refs'],
            aposteriori_refs=data['aposteriori_refs'],
            glyph_range_start=data['glyph_range_start'],
            glyph_range_end=data['glyph_range_end'],
            glyph_count=data['glyph_count'],
            evidence_required=data['evidence_required'],
            evidence_provided=data['evidence_provided'],
            assessed_by=data['assessed_by'],
            assessed_at=data['assessed_at'],
            assessment_method=data['assessment_method'],
            active_constraints=data['active_constraints'],
            advisory_notes=data.get('advisory_notes')
        )


class SPICEDescriptorLayer:
    """
    SPICE Descriptor Layer - Process maturity metadata
    External to vaults, non-cognitive, referential only
    """
    
    J2000_EPOCH = 2451545.0
    J2000_UNIX = 946728000.0
    
    def __init__(self, 
                 storage_path: str = "./spice_layer",
                 matrix_root: str = "./memory_matrix"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        self.matrix_root = Path(matrix_root)
        self.descriptor_file = self.storage_path / "spice_descriptors.jsonl"
        self.index_file = self.storage_path / "spice_index.json"
        
        self.index = self._load_index()
        self._last_descriptor_id = None
        
        self._log_binding()
    
    def _load_index(self) -> Dict:
        if self.index_file.exists():
            with open(self.index_file, 'r') as f:
                return json.load(f)
        return {
            "descriptors": [],
            "process_types": {},
            "capability_distribution": {str(i): 0 for i in range(6)},
            "total_descriptors": 0,
            "last_updated": datetime.now(timezone.utc).isoformat()
        }
    
    def _save_index(self):
        self.index["last_updated"] = datetime.now(timezone.utc).isoformat()
        with open(self.index_file, 'w') as f:
            json.dump(self.index, f, indent=2)
    
    def _log_binding(self):
        binding = {
            "event": "SPICE_LAYER_INITIALIZATION",
            "constitutional_article": "VII",
            "principle": "NON_COGNITIVE_REFERENTIAL_LAYER",
            "binding": "SPICE descriptors are metadata only - never cognitive",
            "vault_contamination": "PREVENTED",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        binding_file = self.storage_path / "constitutional_binding.jsonl"
        with open(binding_file, 'a') as f:
            f.write(json.dumps(binding, separators=(',', ':')) + "\n")
    
    def create_descriptor(self, **kwargs) -> SPICEDescriptor:
        """Create new SPICE descriptor - NON-COGNITIVE metadata only"""
        
        # Convert enums to serializable values
        capability_level = kwargs.get('capability_level')
        if isinstance(capability_level, CapabilityLevel):
            capability_level = capability_level.value
        
        process_outcome = kwargs.get('process_outcome')
        if isinstance(process_outcome, ProcessOutcome):
            process_outcome = process_outcome.value
        
        # Generate descriptor ID
        content = f"{kwargs.get('process_name')}:{kwargs.get('process_version')}:{time.time()}"
        descriptor_id = hashlib.sha256(content.encode()).hexdigest()[:16]
        
        descriptor = SPICEDescriptor(
            descriptor_id=descriptor_id,
            process_name=kwargs.get('process_name', 'unknown'),
            process_version=kwargs.get('process_version', '1.0.0'),
            capability_level=capability_level,
            process_outcome=process_outcome,
            compliance_score=kwargs.get('compliance_score', 0.0),
            apriori_refs=kwargs.get('apriori_refs', []),
            aposteriori_refs=kwargs.get('aposteriori_refs', []),
            glyph_range_start=kwargs.get('glyph_range_start', ''),
            glyph_range_end=kwargs.get('glyph_range_end', ''),
            glyph_count=kwargs.get('glyph_count', 0),
            evidence_required=kwargs.get('evidence_required', []),
            evidence_provided=kwargs.get('evidence_provided', []),
            assessed_by=kwargs.get('assessed_by', 'SYSTEM'),
            assessed_at=kwargs.get('assessed_at', datetime.now(timezone.utc).isoformat()),
            assessment_method=kwargs.get('assessment_method', 'unknown'),
            active_constraints=kwargs.get('active_constraints', []),
            advisory_notes=kwargs.get('advisory_notes')
        )
        
        # Append to immutable chain
        with open(self.descriptor_file, 'a') as f:
            f.write(descriptor.to_json() + "\n")
        
        # Update index
        self.index["descriptors"].append(descriptor_id)
        self.index["total_descriptors"] += 1
        self.index["capability_distribution"][str(capability_level)] += 1
        
        if descriptor.process_name not in self.index["process_types"]:
            self.index["process_types"][descriptor.process_name] = []
        self.index["process_types"][descriptor.process_name].append(descriptor_id)
        
        self._save_index()
        self._last_descriptor_id = descriptor_id
        
        return descriptor
    
    def get_descriptor(self, descriptor_id: str) -> Optional[SPICEDescriptor]:
        """Retrieve descriptor by ID - O(1) via index, O(n) via scan"""
        if not self.descriptor_file.exists():
            return None
        
        with open(self.descriptor_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    data = json.loads(line)
                    if data.get('descriptor_id') == descriptor_id:
                        return SPICEDescriptor(**data)
                except:
                    continue
        return None
    
    def reconstruct_audit_trail(self, descriptor_id: str) -> Dict[str, Any]:
        """
        Full audit trail reconstruction:
        - What happened (process, outcome, glyph range)
        - Why it happened (apriori constraints, evidence)
        - How it happened (capability level, assessment)
        - What was learned (aposteriori refs, advisory)
        """
        descriptor = self.get_descriptor(descriptor_id)
        if not descriptor:
            return {"error": "Descriptor not found"}
        
        return {
            "descriptor": descriptor.to_dict(),
            "what_happened": {
                "process": descriptor.process_name,
                "version": descriptor.process_version,
                "outcome": descriptor.process_outcome,
                "glyph_range": f"{descriptor.glyph_range_start}...{descriptor.glyph_range_end}",
                "glyph_count": descriptor.glyph_count
            },
            "why_it_happened": {
                "apriori_constraints": descriptor.apriori_refs,
                "active_constraints": descriptor.active_constraints,
                "evidence_required": descriptor.evidence_required,
                "evidence_provided": descriptor.evidence_provided
            },
            "how_it_happened": {
                "capability_level": descriptor.capability_level,
                "assessment_method": descriptor.assessment_method,
                "assessed_by": descriptor.assessed_by,
                "assessed_at": descriptor.assessed_at,
                "compliance_score": descriptor.compliance_score
            },
            "what_was_learned": {
                "aposteriori_refs": descriptor.aposteriori_refs,
                "advisory_notes": descriptor.advisory_notes
            }
        }
    
    def get_capability_report(self) -> Dict[str, Any]:
        """Generate capability maturity report"""
        total = self.index["total_descriptors"]
        if total == 0:
            return {"status": "NO_DATA"}
        
        distribution = self.index["capability_distribution"]
        percentages = {k: (v/total)*100 for k, v in distribution.items()}
        
        avg_capability = sum(int(k)*v for k, v in distribution.items()) / total
        
        return {
            "total_processes": total,
            "capability_distribution": distribution,
            "percentages": percentages,
            "average_capability": avg_capability,
            "process_types": list(self.index["process_types"].keys()),
            "last_updated": self.index["last_updated"]
        }


if __name__ == "__main__":
    # Demo usage
    spice = SPICEDescriptorLayer()
    
    descriptor = spice.create_descriptor(
        process_name="DemoProcess",
        capability_level=CapabilityLevel.LEVEL_4,
        process_outcome=ProcessOutcome.COMPLIANT,
        compliance_score=0.95,
        apriori_refs=["apriori:test"],
        glyph_range_start="abc123",
        glyph_range_end="def456",
        assessed_by="TEST"
    )
    
    print(f"Created descriptor: {descriptor.descriptor_id}")
    audit = spice.reconstruct_audit_trail(descriptor.descriptor_id)
    print(json.dumps(audit, indent=2))