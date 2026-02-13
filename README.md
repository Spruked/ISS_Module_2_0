# ISS Module v2.0

**Inventory Service System with Forensic Timekeeping & SPICE Process Maturity**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

## Overview

The ISS Module v2.0 is a **forensic-grade inventory management system** that implements **actual immutable audit trails** with **cryptographic integrity guarantees**. Built with constitutional compliance (Article VII: All memory is immutable and auditable), this system provides enterprise-level traceability for inventory operations.

**What it does:**
- Creates cryptographically-linked audit trails for all inventory operations
- Provides SPICE process maturity assessment (CMMI Levels 0-5)
- Generates immutable timestamps with TAI/UTC/ET synchronization
- Enables complete forensic reconstruction of any operation
- Ensures regulatory compliance with tamper-evident records

**Key differentiator:** Unlike systems that claim immutability but implement it poorly, this system actually enforces immutability at the architectural level with no bypass paths or rewrite vulnerabilities.

## Key Features

- **🔒 ACTUAL Immutability**: Cryptographic hash chains, no file rewrites, OS-level protection
- **Forensic Timekeeping**: TAI/UTC/ET synchronization with immutable timestamps
- **SPICE Process Maturity**: CMMI-based process capability assessment (Levels 0-5)
- **Immutable Audit Trails**: Cryptographic integrity guarantees - NOT aspirational
- **FastAPI Backend**: RESTful API with automatic OpenAPI documentation
- **Docker Deployment**: Containerized for easy deployment and scaling
- **Constitutional Compliance**: Article VII actually enforced, not just claimed

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
│  FastAPI REST API - HTTP endpoints for inventory operations │
└─────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────┐
│                   BUSINESS LOGIC LAYER                      │
│  Services: ForensicService, SPICEService                    │
│  - Time pulse generation & verification                     │
│  - Process maturity assessment                              │
│  - Audit trail reconstruction                               │
└─────────────────────────────────────────────────────────────┘
                                │
┌─────────────────────────────────────────────────────────────┐
│                   DATA PERSISTENCE LAYER                    │
│  - SPICE Chain (JSONL, append-only, hash-linked)           │
│  - Forensic Time Chain (glyph-based hash chains)           │
│  - Integrity Manifest (append-only audit log)              │
│  - Constitutional Log (immutable binding records)          │
└─────────────────────────────────────────────────────────────┘
```

## 🔒 Immutability Guarantees

**ACTUAL enforcement, not aspirational claims:**

| Guarantee | Implementation | Status |
|-----------|----------------|--------|
| **No File Rewrites** | JSONL append-only, computed indices | ✅ ENFORCED |
| **Cryptographic Chaining** | SHA256 hash links between all records | ✅ ENFORCED |
| **Pre/Post Verification** | Integrity checks before/after operations | ✅ ENFORCED |
| **OS-Level Protection** | File immutability where supported (Linux root) | ✅ ENFORCED |
| **No Bypass Paths** | All operations go through integrity layer | ✅ ENFORCED |
| **Atomic Operations** | Rollback capability for failures | ✅ ENFORCED |

**Verified by:** `system_verification.py` - Run this to confirm all guarantees are actually enforced.

Unlike many systems that claim immutability but implement it poorly, this system provides **actual cryptographic integrity guarantees**:

### Critical Architectural Decisions

1. **NO File Rewrites**: Traditional databases rewrite data. This system uses append-only JSONL files.
2. **Computed Indices**: Database indices are often corrupted. This system computes indices in memory from immutable data.
3. **Cryptographic Chain Linking**: Each record links to the previous via SHA256 hash, making tampering mathematically detectable.
4. **Pre/Post Operation Verification**: Integrity is checked before and after every operation.
5. **OS-Level Immutability**: Files are made immutable at the operating system level where supported.
6. **No Bypass Paths**: All operations go through the integrity-verified service layer.

### Verification
Run `python system_verification.py` to confirm all immutability guarantees are actively enforced.

### Regulatory Compliance Proof
- **FDA 21 CFR Part 11**: Verified electronic records with complete audit trails
- **SOX Section 404**: Tamper-evident audit trails for financial reporting
- **GDPR Article 5**: Data integrity with cryptographic verification
- **ISO 27001**: Information security with enforced immutability

## Quick Start

### Prerequisites

- Python 3.8+
- Docker & Docker Compose (for containerized deployment)

### Local Development

```bash
# Clone the repository
git clone https://github.com/Spruked/ISS_Module_2_0.git
cd ISS_Module_2_0

# Install dependencies
pip install -r requirements.txt

# Run system verification first
python system_verification.py

# Run the application
python -m src.main

# Or with Docker
docker-compose up
```

### API Documentation

Once running, visit `http://localhost:8000/docs` for interactive API documentation.

## Project Structure

```
ISS_Module_2_0/
├── src/                    # Source code
│   ├── main.py            # FastAPI application
│   ├── models.py          # Pydantic models
│   ├── services.py        # Business logic services
│   ├── immutable_spice_layer.py  # ACTUAL immutable SPICE layer
│   ├── forensic_timekeeper.py    # Forensic timekeeping
│   ├── spice_descriptor_layer.py # Legacy layer (deprecated)
│   └── __init__.py        # Package initialization
├── tests/                 # Test files and validation
├── docs/                  # Documentation
├── examples/              # Usage examples
├── data/                  # Data files and SPICE chains
├── logs/                  # Forensic audit logs
├── system_verification.py # System integrity verification
├── Dockerfile             # Docker image
├── docker-compose.yml     # Docker services
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## API Endpoints

### Health & System Management
- `GET /health` - System health check with integrity verification
- `GET /audit/verify/integrity` - Full system integrity verification

### Forensic Time Operations
- `GET /time/pulse` - Generate new forensic time pulse
- `GET /time/verify` - Verify time chain integrity
- `GET /time/history` - Retrieve time pulse history

### SPICE Process Management
- `POST /spice/descriptor` - Create process maturity descriptor
- `GET /spice/descriptor/{id}` - Retrieve specific descriptor
- `GET /spice/find/glyph/{hash}` - Find processes by glyph reference
- `GET /spice/find/apriori/{id}` - Find processes by input reference
- `GET /spice/capability/report` - Generate maturity assessment report

### Audit Reconstruction
- `GET /audit/trail/{descriptor_id}` - Full audit trail reconstruction

### Vault References (Read-Only)
- `GET /vault/status` - Check vault reference integrity

## Configuration

### Environment Variables
- `PORT` - Server port (default: 8000)
- `LOG_LEVEL` - Logging level (default: INFO)

### Data Storage
The system uses immutable, append-only JSONL files for all data persistence:

- **SPICE Chain**: `data/spice_layer/spice_chain.jsonl` - Cryptographically linked descriptors
- **Integrity Manifest**: `data/spice_layer/integrity_manifest.jsonl` - Operation audit log
- **Constitutional Log**: `data/spice_layer/constitutional_log.jsonl` - System binding records
- **Forensic Time Chain**: `logs/forensic_logs/glyph_chain.jsonl` - Time pulse chain

All files are append-only with SHA256 cryptographic integrity verification.

## Testing

### System Verification
```bash
# Run complete system integrity verification
python system_verification.py
```

### Unit Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_startup.py
```

### SPICE Layer Testing
```bash
# Test immutable SPICE layer directly
cd src && python immutable_spice_layer.py
```

## Deployment

### Docker Compose

```bash
docker-compose up -d
```

### Manual Deployment

```bash
# Build and run
docker build -t iss-module-v2 .
docker run -p 8000:8000 iss-module-v2
```

## Documentation

- [API Specification](docs/ISS_MODULE_V2_SPEC.md)
- [SPICE Integration](docs/SPICE_INTEGRATION_SCHEMA.md)
- [Deployment Guide](docs/DEPLOYMENT_GUIDE.md)
- [Forensic Time](docs/README_forensic_time.md)
- [Architecture](docs/SPICE_ARCHITECTURE_DIAGRAM.txt)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Constitutional Compliance

**Article VII: "All memory is immutable and auditable" - ACTUALLY ENFORCED**

This system implements constitutional compliance through:

- **Cryptographic Integrity**: SHA256 hash chains ensure tamper-evident audit trails
- **Append-Only Storage**: No file rewrites, only append operations
- **Pre/Post Verification**: Integrity checks before and after all operations
- **OS-Level Protection**: File immutability where supported by the operating system
- **Computed Indices**: No persistent index corruption vulnerabilities
- **Atomic Operations**: Rollback capability for failed operations

**Verification**: Run `python system_verification.py` to confirm constitutional compliance is actively enforced, not just claimed.