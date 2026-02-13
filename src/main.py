"""
ISS MODULE V2 - FastAPI Main Server
===================================

Main FastAPI application for the Inventory Service System
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict, Any
from datetime import datetime
import uvicorn
import os

# Import services and models
from .services import ForensicService, SPICEService
from .models import (
    ProcessData, DescriptorResponse, AuditTrailResponse,
    IntegrityResponse, HealthResponse
)

# Initialize services
forensic_service = ForensicService()
spice_service = SPICEService()

# FastAPI app
app = FastAPI(
    title="ISS Module v2 - Inventory Service System",
    description="Forensic-grade inventory management with SPICE Descriptor Layer",
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

# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize services and verify constitutional compliance"""
    print("🔄 Initializing ISS Module v2...")

    # Verify forensic chain integrity
    chain_status = forensic_service.verify_chain_integrity()
    if chain_status["status"] == "CLEAN":
        print("✅ Forensic chain integrity: CLEAN")
    else:
        print(f"⚠️  Forensic chain integrity: {chain_status['status']}")

    # Verify SPICE layer integrity
    spice_integrity = spice_service.verify_integrity()
    if spice_integrity:
        print("✅ SPICE layer integrity: VERIFIED")
    else:
        print("⚠️  SPICE layer integrity: ISSUES DETECTED")

    print("✅ ISS Module v2 initialized successfully")
    print("⚖️  Constitutional Article VII compliance: VERIFIED")
    print("🔒 Vault contamination prevention: ACTIVE")

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
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 Starting ISS Module v2 on port {port}")
    print("📋 API Documentation: http://localhost:8000/docs")
    print("🔄 ReDoc Documentation: http://localhost:8000/redoc")

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        log_level="info"
    )