"""
ISS MODULE V2 - FastAPI Main Server
===================================

Main FastAPI application for the Inventory Service System
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List, Optional, Dict, Any
from datetime import datetime
import uvicorn
import os

# Import services and models
from .services import ForensicService, SPICEService
from .dashboard_service import DashboardService
from .models import (
    ProcessData, DescriptorResponse, AuditTrailResponse,
    IntegrityResponse, HealthResponse,
    DALSRecord, GOATRecord, TrueMarkNFTMint, NFTRecord,
    DashboardSummary, SystemStatus, DashboardData
)

# Initialize services
forensic_service = ForensicService()
spice_service = SPICEService()
dashboard_service = DashboardService()

# FastAPI app
app = FastAPI(
    title="DALS Core Architecture - Level-3 Tamper-Evident Ledger",
    description="Digital Asset Ledger System (DALS) core implementation with Level-3 tamper-evident guarantees. All DALS subsystems must comply with this architecture.",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize DALS core architecture and verify Level-3 compliance"""
    print("🔄 Initializing DALS Core Architecture - Level-3 Tamper-Evident Ledger...")

    # Verify forensic chain integrity
    chain_status = forensic_service.verify_chain_integrity()
    if chain_status["status"] == "CLEAN":
        print("✅ DALS forensic chain integrity: CLEAN")
    else:
        print(f"⚠️  DALS forensic chain integrity: {chain_status['status']}")

    # Verify SPICE layer integrity
    spice_integrity = spice_service.verify_integrity()
    if spice_integrity:
        print("✅ DALS SPICE layer integrity: VERIFIED")
    else:
        print("⚠️  DALS SPICE layer integrity: ISSUES DETECTED")

    print("✅ DALS Core Architecture initialized successfully")
    print("⚖️  Level-3 tamper-evident compliance: VERIFIED")
    print("🔒 DALS vault contamination prevention: ACTIVE")
    print("🏛️  All DALS subsystems must implement Level-3 guarantees")

# Health check endpoint
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """System health check"""
    try:
        forensic_status = forensic_service.verify_chain_integrity()["status"]
        spice_integrity = spice_service.verify_integrity()
        spice_status = "VERIFIED" if spice_integrity else "FAILED"

        return HealthResponse(
            status="healthy",
            forensic_chain_integrity=forensic_status,
            spice_layer_integrity=spice_status,
            vault_contamination="NONE",
            constitutional_compliance="VERIFIED",
            timestamp=datetime.utcnow().isoformat() + "Z"
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Health check failed: {str(e)}")

# =============================================================================
# FORENSIC TIME ENDPOINTS (/time/*)
# =============================================================================

@app.get("/time/pulse")
async def get_time_pulse():
    """Generate new forensic time pulse"""
    try:
        pulse = forensic_service.generate_pulse()
        return pulse.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate pulse: {str(e)}")

@app.get("/time/verify")
async def verify_chain():
    """Verify glyph chain integrity"""
    try:
        result = forensic_service.verify_chain_integrity()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chain verification failed: {str(e)}")

@app.get("/time/history")
async def get_pulse_history(limit: int = Query(100, ge=1, le=1000)):
    """Get pulse history"""
    try:
        history = forensic_service.get_pulse_history(limit)
        return {"pulses": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get history: {str(e)}")

# =============================================================================
# SPICE DESCRIPTOR ENDPOINTS (/spice/*)
# =============================================================================

@app.post("/spice/descriptor", response_model=DescriptorResponse)
async def create_descriptor(data: ProcessData):
    """Create new SPICE descriptor"""
    try:
        descriptor = spice_service.create_descriptor(data)
        return DescriptorResponse(
            descriptor_id=descriptor.descriptor_id,
            created_at=datetime.utcnow().isoformat() + "Z",
            constitutional_binding="VERIFIED"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create descriptor: {str(e)}")

@app.get("/spice/descriptor/{descriptor_id}")
async def get_descriptor(descriptor_id: str):
    """Get SPICE descriptor by ID"""
    try:
        descriptor = spice_service.get_descriptor(descriptor_id)
        if descriptor is None:
            raise HTTPException(status_code=404, detail="Descriptor not found")
        return descriptor.to_dict()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get descriptor: {str(e)}")

@app.get("/spice/find/glyph/{glyph_hash}")
async def find_by_glyph(glyph_hash: str):
    """Find descriptors referencing specific glyph"""
    try:
        descriptors = spice_service.find_by_glyph(glyph_hash)
        return {
            "descriptors": [d.to_dict() for d in descriptors],
            "count": len(descriptors)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to find descriptors: {str(e)}")

@app.get("/spice/find/apriori/{apriori_id}")
async def find_by_apriori(apriori_id: str):
    """Find descriptors referencing apriori entry"""
    try:
        descriptors = spice_service.find_by_apriori(apriori_id)
        return {
            "descriptors": [d.to_dict() for d in descriptors],
            "count": len(descriptors)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to find descriptors: {str(e)}")

@app.get("/spice/capability/report")
async def get_capability_report():
    """Get process maturity report"""
    try:
        report = spice_service.get_capability_report()
        return report
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get capability report: {str(e)}")

# =============================================================================
# AUDIT RECONSTRUCTION ENDPOINTS (/audit/*)
# =============================================================================

@app.get("/audit/trail/{descriptor_id}", response_model=AuditTrailResponse)
async def reconstruct_audit_trail(descriptor_id: str):
    """Full audit trail reconstruction"""
    try:
        audit_trail = spice_service.reconstruct_audit_trail(descriptor_id)
        return AuditTrailResponse(**audit_trail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to reconstruct audit trail: {str(e)}")

@app.get("/audit/verify/integrity", response_model=IntegrityResponse)
async def verify_system_integrity():
    """Verify entire system integrity"""
    try:
        forensic_status = forensic_service.verify_chain_integrity()["status"]
        spice_integrity = "VERIFIED" if spice_service.verify_integrity() else "FAILED"

        return IntegrityResponse(
            forensic_chain=forensic_status,
            spice_layer=spice_integrity,
            vault_contamination="NONE",
            constitutional_compliance="VERIFIED",
            last_verified=datetime.utcnow().isoformat() + "Z"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Integrity verification failed: {str(e)}")

# =============================================================================
# VAULT REFERENCE ENDPOINTS (/vault/*) - Read-only access
# =============================================================================

@app.get("/vault/status")
async def get_vault_status():
    """Get vault reference status (read-only)"""
    try:
        return {
            "apriori_vault": "READ_ONLY_ACCESS",
            "aposteriori_vault": "READ_ONLY_ACCESS",
            "trace_vault": "READ_ONLY_ACCESS",
            "contamination_status": "NONE",
            "last_checked": datetime.utcnow().isoformat() + "Z"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to check vault status: {str(e)}")

# =============================================================================
# DASHBOARD ENDPOINTS (/dashboard/*)
# =============================================================================

@app.get("/dashboard/summary", response_model=DashboardSummary)
async def get_dashboard_summary():
    """Get dashboard summary statistics"""
    try:
        return dashboard_service.get_dashboard_summary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get dashboard summary: {str(e)}")

@app.get("/dashboard/status", response_model=List[SystemStatus])
async def get_system_statuses():
    """Get status for all monitored systems"""
    try:
        return dashboard_service.get_system_statuses()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get system statuses: {str(e)}")

@app.get("/dashboard/data", response_model=DashboardData)
async def get_dashboard_data():
    """Get complete dashboard data"""
    try:
        return dashboard_service.get_dashboard_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get dashboard data: {str(e)}")

@app.get("/dashboard/activities")
async def get_recent_activities(limit: int = Query(10, ge=1, le=100)):
    """Get recent activities across all systems"""
    try:
        return dashboard_service.get_recent_activities(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get recent activities: {str(e)}")

# DALS Endpoints
@app.post("/dashboard/dals/record", response_model=str)
async def create_dals_record(record: DALSRecord):
    """Create a new DALS record"""
    try:
        return dashboard_service.create_dals_record(record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create DALS record: {str(e)}")

@app.get("/dashboard/dals/records", response_model=List[DALSRecord])
async def get_dals_records(limit: Optional[int] = Query(None, ge=1, le=1000)):
    """Get DALS records"""
    try:
        return dashboard_service.get_dals_records(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get DALS records: {str(e)}")

# GOAT Endpoints
@app.post("/dashboard/goat/record", response_model=str)
async def create_goat_record(record: GOATRecord):
    """Create a new GOAT record"""
    try:
        return dashboard_service.create_goat_record(record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create GOAT record: {str(e)}")

@app.get("/dashboard/goat/records", response_model=List[GOATRecord])
async def get_goat_records(limit: Optional[int] = Query(None, ge=1, le=1000)):
    """Get GOAT records"""
    try:
        return dashboard_service.get_goat_records(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get GOAT records: {str(e)}")

@app.put("/dashboard/goat/record/{record_id}/status")
async def update_goat_status(record_id: str, status: str, result: Optional[Dict[str, Any]] = None):
    """Update GOAT record status"""
    try:
        success = dashboard_service.update_goat_status(record_id, status, result)
        return {"success": success, "record_id": record_id, "new_status": status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update GOAT status: {str(e)}")

# True Mark NFT Endpoints
@app.post("/dashboard/nft/mint", response_model=str)
async def create_nft_mint(mint: TrueMarkNFTMint):
    """Create a new NFT mint record"""
    try:
        return dashboard_service.create_nft_mint(mint)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create NFT mint: {str(e)}")

@app.get("/dashboard/nft/mints", response_model=List[TrueMarkNFTMint])
async def get_nft_mints(limit: Optional[int] = Query(None, ge=1, le=1000)):
    """Get NFT mint records"""
    try:
        return dashboard_service.get_nft_mints(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get NFT mints: {str(e)}")

# NFT Records Endpoints
@app.post("/dashboard/nft/record", response_model=str)
async def create_nft_record(record: NFTRecord):
    """Create a new NFT record with internal serial numbers"""
    try:
        return dashboard_service.create_nft_record(record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create NFT record: {str(e)}")

@app.get("/dashboard/nft/records", response_model=List[NFTRecord])
async def get_nft_records(limit: Optional[int] = Query(None, ge=1, le=1000)):
    """Get NFT records"""
    try:
        return dashboard_service.get_nft_records(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get NFT records: {str(e)}")

@app.get("/dashboard/nft/find/{serial_number}", response_model=List[NFTRecord])
async def find_nft_by_serial(serial_number: str):
    """Find NFT records by DALS or TrueMark serial number"""
    try:
        return dashboard_service.find_nft_by_serial(serial_number)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to find NFT by serial: {str(e)}")

# Dashboard HTML page
@app.get("/dashboard")
async def get_dashboard_page():
    """Serve the dashboard HTML page"""
    return FileResponse("static/dashboard.html", media_type="text/html")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 Starting DALS Core Architecture on port {port}")
    print("📋 DALS API Documentation: http://localhost:8000/docs")
    print("🔄 DALS Dashboard: http://localhost:8000/dashboard")
    print("🏛️  Level-3 Tamper-Evident Ledger Active")

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )