"""
ISS MODULE V2 - Pydantic Models
===============================

Request/response models for the FastAPI application
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

# Request Models
class ProcessData(BaseModel):
    process_name: str = Field(..., description="Name of the process")
    process_version: str = Field(..., description="Version of the process")
    capability_level: int = Field(..., ge=0, le=5, description="SPICE capability level")
    process_outcome: str = Field(..., description="Process outcome")
    compliance_score: float = Field(..., ge=0.0, le=1.0, description="Compliance score")
    apriori_refs: List[str] = Field(default_factory=list, description="Apriori vault references")
    aposteriori_refs: List[str] = Field(default_factory=list, description="Aposteriori vault references")
    glyph_range_start: str = Field(..., description="Starting glyph hash")
    glyph_range_end: str = Field(..., description="Ending glyph hash")
    glyph_count: int = Field(..., gt=0, description="Number of glyphs in range")
    evidence_required: List[str] = Field(..., description="Required evidence")
    evidence_provided: List[str] = Field(..., description="Provided evidence")
    assessed_by: str = Field(..., description="Assessment authority")
    assessment_method: str = Field(..., description="Assessment method")
    active_constraints: List[str] = Field(..., description="Active constraints")

# Response Models
class DescriptorResponse(BaseModel):
    descriptor_id: str
    created_at: str
    constitutional_binding: str

class AuditTrailResponse(BaseModel):
    what_happened: Dict[str, Any]
    why_it_happened: Dict[str, Any]
    how_it_happened: Dict[str, Any]
    what_was_learned: Dict[str, Any]
    vault_pointers: Dict[str, str]

class IntegrityResponse(BaseModel):
    forensic_chain: str
    spice_layer: str
    vault_contamination: str
    constitutional_compliance: str
    last_verified: str

class HealthResponse(BaseModel):
    status: str
    forensic_chain_integrity: str
    spice_layer_integrity: str
    vault_contamination: str
    constitutional_compliance: str
    timestamp: str