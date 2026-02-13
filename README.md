# ISS Module v2.0 - DALS Core Architecture

**Level-3 Tamper-Evident Ledger - Foundation for Digital Asset Ledger System (DALS)**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![Maturity](https://img.shields.io/badge/maturity-Level_3-orange.svg)]()
[![Tamper-Evident](https://img.shields.io/badge/tamper_evident-SHA256-green.svg)]()
[![DALS Core](https://img.shields.io/badge/DALS-Core_Architecture-blue.svg)]()

## Overview

The ISS Module v2.0 is the **core architecture for the Digital Asset Ledger System (DALS)**, implementing a **Level-3 tamper-evident ledger** that provides enterprise-level traceability for all digital asset operations.

**This Level-3 architecture is mandatory for all DALS subsystems**, replacing previous implementations with guaranteed tamper-evident properties.

**What it actually does:**
- Creates cryptographically-linked audit trails for all DALS operations
- Provides SPICE process maturity assessment (CMMI Levels 0-5)
- Generates immutable timestamps with TAI/UTC/ET synchronization
- Enables complete forensic reconstruction of any operation
- Ensures tamper-evident records through cryptographic integrity

**Key differentiator:** Unlike systems that claim immutability but implement it poorly, this system actually enforces tamper-evident properties at the architectural level with no bypass paths or rewrite vulnerabilities.

## DALS Integration

**This ISS Module v2.0 becomes the foundation of DALS:**

| Component | Integration | Compliance Level |
|-----------|-------------|------------------|
| **DALS Core** | Direct replacement for current ISS module | Level-3 Mandatory |
| **All Subsystems** | Must implement Level-3 tamper-evident guarantees | Level-3 Mandatory |
| **GOAT Operations** | Logged to tamper-evident ledger | Level-3 Enforced |
| **True Mark NFT** | Minting records with serial traceability | Level-3 Enforced |
| **NFT Records** | Internal DALS/TrueMark serial references | Level-3 Enforced |
| **Dashboard** | Real-time monitoring of all DALS components | Level-3 Verified |

**All DALS subsystems must comply with Level-3 tamper-evident architecture.**

## DALS Subsystem Compliance Requirements

**All DALS components must implement Level-3 tamper-evident guarantees:**

### 🔒 Mandatory Level-3 Implementation

| Subsystem | Requirement | Enforcement |
|-----------|-------------|-------------|
| **Asset Ledger** | SHA256 hash-chained append-only records | Mandatory |
| **GOAT Operations** | All operations logged to tamper-evident chain | Mandatory |
| **True Mark NFT Mint** | Minting records with cryptographic integrity | Mandatory |
| **NFT Records** | Internal serial number references verified | Mandatory |
| **Transfer Operations** | Atomic operations with integrity checks | Mandatory |
| **Audit Systems** | Pre/post verification on all changes | Mandatory |

### 📋 Implementation Checklist for DALS Subsystems

**Every DALS subsystem must provide:**

- [ ] **Append-Only Storage**: No file rewrites, only append operations
- [ ] **Cryptographic Chaining**: SHA256 hash links between all records
- [ ] **Pre/Post Verification**: Integrity checks before/after operations
- [ ] **Atomic Operations**: Rollback capability for failures
- [ ] **No Bypass Paths**: All operations through integrity layer
- [ ] **Tamper-Evident Logging**: All activities logged to SPICE layer
- [ ] **Serial Number Integration**: Cross-references to DALS/TrueMark serials
- [ ] **Dashboard Integration**: Real-time monitoring and health reporting

### 🔄 Migration Path

**Current ISS Module → DALS Core Architecture:**

1. **Phase 1**: Deploy Level-3 tamper-evident ledger as DALS core
2. **Phase 2**: Migrate all subsystems to Level-3 compliance
3. **Phase 3**: Decommission non-compliant legacy components
4. **Phase 4**: Full DALS ecosystem operating on Level-3 guarantees

**All subsystems must pass Level-3 verification before integration.**

## Key Features

- **🔒 Level-3 Tamper-Evident**: Cryptographic hash chains, append-only storage, integrity verification
- **Forensic Timekeeping**: TAI/UTC/ET synchronization with immutable timestamps
- **SPICE Process Maturity**: CMMI-based process capability assessment (Levels 0-5)
- **Cryptographic Audit Trails**: SHA256 hash-chained, tamper-evident ledger
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

## 🔒 Tamper-Evident Guarantees

**Level-3 Implementation (Actually Enforced):**

| Guarantee | Implementation | Status |
|-----------|----------------|--------|
| **Append-Only Storage** | JSONL files, no rewrites allowed | ✅ ENFORCED |
| **Cryptographic Chaining** | SHA256 hash links between all records | ✅ ENFORCED |
| **Pre/Post Verification** | Integrity checks before/after operations | ✅ ENFORCED |
| **OS-Level Protection** | File immutability where supported (Linux root) | ✅ ENFORCED |
| **No Bypass Paths** | All operations go through integrity layer | ✅ ENFORCED |
| **Atomic Operations** | Rollback capability for failures | ✅ ENFORCED |

**Verified by:** `system_verification.py` - Run this to confirm tamper-evident properties are actively enforced.

### What This System Actually Provides

**✅ Legitimate Achievements:**
- Append-only JSONL with hash chaining
- Pre/post integrity verification
- No persistent index rewrites
- Deterministic reconstruction
- Crash-durable writes

**❌ Not Provided (Would Require Additional Implementation):**
- HMAC with key separation
- Digital signatures
- External trust anchoring
- Manifest cryptographic chaining
- Boot-time hard failure
- Key rotation procedures

### Maturity Level Assessment

**Current: Level 3** - Hash-chained, append-only, tamper-evident ledger
**Gap to Level 4:** HMAC/signed with key separation
**Gap to Level 5:** External trust anchor, full forensic resistance

### Important: What This System Is NOT

**This system is a serious tamper-evident ledger. It is NOT:**

| False Claim | Reality | What Would Be Required |
|-------------|---------|----------------------|
| "FDA 21 CFR Part 11 compliant" | Not compliant | Unique user IDs, e-signatures, SOPs, validation docs |
| "SOX compliant" | Not compliant | Documented controls, segregation of duties, external audit |
| "GDPR compliant" | Not compliant | Data minimization, right to erasure, retention policies |
| "ISO 27001 compliant" | Not compliant | ISMS framework, risk register, key management policy |
| "Attacker-resistant" | Honest-host assumption | Privileged attacker resistance, external anchoring |
| "Certified compliant system" | Code ≠ Certification | Formal certification process and documentation |

**Code ≠ Certification. Architecture ≠ Compliance framework.**

### Path to Higher Maturity Levels (If Required)

1. **HMAC implementation** with key stored in separate trust boundary
2. **Digital signatures** using asymmetric keys
3. **External anchoring** to public timestamping service
4. **Manifest chaining** - integrate into main cryptographic chain
5. **Boot-time hard fail** - system refuses to start if integrity check fails
6. **Key rotation model** - documented procedures for key lifecycle
7. **Role separation** - distinct writer/verifier/admin roles

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

### Dashboard

The system includes a comprehensive dashboard for monitoring DALS, GOAT, True Mark NFT Mint, and NFT records:

- **Live Dashboard**: `http://localhost:8000/dashboard` - Interactive monitoring interface
- **System Metrics**: Real-time statistics for all monitored systems
- **NFT Serial Lookup**: Search NFTs by DALS or TrueMark serial numbers
- **Activity Monitoring**: Recent activities across all systems
- **Health Status**: System health indicators and alerts

#### Generate Sample Data

```bash
# Generate sample data for testing the dashboard
python generate_dashboard_data.py
```

#### Dashboard API Endpoints

- `GET /dashboard/data` - Complete dashboard data
- `GET /dashboard/summary` - System summary statistics
- `GET /dashboard/status` - Individual system statuses
- `GET /dashboard/activities` - Recent activities
- `POST /dashboard/dals/record` - Create DALS record
- `POST /dashboard/goat/record` - Create GOAT record
- `POST /dashboard/nft/mint` - Create NFT mint record
- `POST /dashboard/nft/record` - Create NFT record
- `GET /dashboard/nft/find/{serial}` - Find NFTs by serial number

## Project Structure

```
DALS_Core_Architecture/
├── src/                    # DALS Core Implementation
│   ├── main.py            # FastAPI application (DALS API)
│   ├── models.py          # Pydantic models (DALS data structures)
│   ├── services.py        # Business logic services (DALS operations)
│   ├── immutable_spice_layer.py  # Level-3 tamper-evident core
│   ├── dashboard_service.py      # DALS monitoring & control
│   ├── forensic_timekeeper.py    # Immutable timestamping
│   ├── spice_descriptor_layer.py # Legacy layer (deprecated)
│   └── __init__.py        # Package initialization
├── data/                  # DALS persistent data
│   ├── spice_layer/       # Tamper-evident chain storage
│   └── dashboard/         # System monitoring data
├── logs/                  # DALS audit logs
├── static/                # DALS dashboard interface
├── tests/                 # DALS compliance tests
├── docs/                  # DALS documentation
├── examples/              # DALS usage examples
├── system_verification.py # Level-3 compliance verification
├── generate_dashboard_data.py # DALS test data generation
├── Dockerfile             # DALS containerization
├── docker-compose.yml     # DALS service orchestration
├── requirements.txt       # DALS dependencies
├── .gitignore            # DALS ignore rules
└── README.md             # This DALS core documentation
```

## DALS Core API Endpoints

### System Management & Compliance
- `GET /health` - DALS system health with Level-3 verification
- `GET /audit/verify/integrity` - Full DALS integrity verification

### Forensic Time Operations (DALS Core)
- `GET /time/pulse` - Generate DALS forensic time pulse
- `GET /time/verify` - Verify DALS time chain integrity
- `GET /time/history` - DALS time pulse history

### SPICE Process Management (DALS Core)
- `POST /spice/descriptor` - Create DALS process maturity descriptor
- `GET /spice/descriptor/{id}` - Retrieve DALS process descriptor
- `GET /spice/find/glyph/{hash}` - Find DALS processes by glyph reference
- `GET /spice/find/apriori/{id}` - Find DALS processes by input reference
- `GET /spice/capability/report` - DALS maturity assessment report

### DALS Subsystem Monitoring
- `GET /dashboard` - DALS monitoring dashboard (HTML)
- `GET /dashboard/summary` - DALS subsystem statistics
- `GET /dashboard/status` - Individual DALS component statuses
- `GET /dashboard/data` - Complete DALS monitoring data
- `GET /dashboard/activities` - Recent DALS activities

### DALS Record Management
- `POST /dashboard/dals/record` - Create DALS asset record
- `GET /dashboard/dals/records` - Get DALS asset records
- `POST /dashboard/goat/record` - Create DALS GOAT operation record
- `GET /dashboard/goat/records` - Get DALS GOAT operation records
- `POST /dashboard/nft/mint` - Create DALS True Mark NFT mint
- `GET /dashboard/nft/mints` - Get DALS NFT mint records
- `POST /dashboard/nft/record` - Create DALS NFT record with serial refs
- `GET /dashboard/nft/records` - Get DALS NFT records
- `GET /dashboard/nft/find/{serial}` - Find DALS NFTs by serial number

### Audit Reconstruction (DALS Core)
- `GET /audit/trail/{descriptor_id}` - Full DALS audit trail reconstruction

### Vault References (DALS Core)
- `GET /vault/status` - DALS vault reference integrity

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

**Important**: This provides **Level-3 tamper-evident guarantees** suitable for regulated environments when deployed within a compliant operational framework. It is not a certified compliant system.