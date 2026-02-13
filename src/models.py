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

# Dashboard Models
class DALSRecord(BaseModel):
    """Digital Asset Ledger System Record"""
    record_id: str = Field(..., description="Unique DALS record identifier")
    asset_type: str = Field(..., description="Type of digital asset")
    asset_hash: str = Field(..., description="Cryptographic hash of the asset")
    owner_id: str = Field(..., description="Current owner identifier")
    transfer_history: List[Dict[str, Any]] = Field(default_factory=list, description="Transfer history")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    created_at: str = Field(..., description="Creation timestamp")
    last_updated: str = Field(..., description="Last update timestamp")

class GOATRecord(BaseModel):
    """GOAT System Record"""
    record_id: str = Field(..., description="Unique GOAT record identifier")
    operation_type: str = Field(..., description="Type of operation")
    status: str = Field(..., description="Current status")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Operation parameters")
    result: Optional[Dict[str, Any]] = Field(None, description="Operation result")
    execution_time: Optional[float] = Field(None, description="Execution time in seconds")
    created_at: str = Field(..., description="Creation timestamp")
    completed_at: Optional[str] = Field(None, description="Completion timestamp")

class TrueMarkNFTMint(BaseModel):
    """True Mark NFT Minting Record"""
    mint_id: str = Field(..., description="Unique mint identifier")
    nft_contract: str = Field(..., description="NFT contract address")
    token_id: str = Field(..., description="NFT token ID")
    serial_number: str = Field(..., description="True Mark serial number")
    metadata_uri: str = Field(..., description="IPFS or metadata URI")
    minter_address: str = Field(..., description="Address that minted the NFT")
    royalty_percentage: float = Field(..., ge=0.0, le=100.0, description="Royalty percentage")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="NFT attributes")
    created_at: str = Field(..., description="Minting timestamp")

class NFTRecord(BaseModel):
    """NFT Record with Internal Serial Numbers"""
    record_id: str = Field(..., description="Unique NFT record identifier")
    nft_info: TrueMarkNFTMint = Field(..., description="NFT minting information")
    dals_serial_numbers: List[str] = Field(default_factory=list, description="Associated DALS serial numbers")
    truemark_serial_numbers: List[str] = Field(default_factory=list, description="Associated True Mark serial numbers")
    ownership_chain: List[Dict[str, Any]] = Field(default_factory=list, description="Ownership transfer history")
    verification_status: str = Field(..., description="Verification status")
    last_verified: str = Field(..., description="Last verification timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

# Dashboard Response Models
class DashboardSummary(BaseModel):
    """Dashboard summary statistics"""
    total_dals_records: int
    total_goat_records: int
    total_nft_mints: int
    total_nft_records: int
    active_operations: int
    system_health: str
    last_updated: str

class SystemStatus(BaseModel):
    """Individual system status"""
    system_name: str
    status: str  # "healthy", "warning", "error"
    record_count: int
    last_activity: str
    uptime_percentage: float
    alerts: List[str] = Field(default_factory=list)

class DashboardData(BaseModel):
    """Complete dashboard data"""
    summary: DashboardSummary
    system_statuses: List[SystemStatus]
    recent_activities: List[Dict[str, Any]]
    alerts: List[Dict[str, Any]]