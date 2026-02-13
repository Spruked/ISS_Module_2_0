# ISS Module v2.0

**Inventory Service System with Forensic Timekeeping & SPICE Process Maturity**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

## Overview

The ISS Module v2.0 is a forensic-grade inventory management system that implements immutable audit trails and SPICE process maturity metadata. Built with constitutional compliance in mind (Article VII: All memory is immutable and auditable), this system provides enterprise-level traceability for inventory operations.

## Key Features

- **Forensic Timekeeping**: TAI/UTC/ET synchronization with immutable timestamps
- **SPICE Process Maturity**: CMMI-based process capability assessment (Levels 0-5)
- **Immutable Audit Trails**: Cryptographic hash chains for complete traceability
- **FastAPI Backend**: RESTful API with automatic OpenAPI documentation
- **Docker Deployment**: Containerized for easy deployment and scaling
- **Constitutional Compliance**: Designed for regulatory environments requiring immutable records

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   FastAPI       │    │  SPICE Layer     │    │  Forensic Time  │
│   REST API      │◄──►│  Process         │◄──►│  TAI/UTC/ET     │
│                 │    │  Maturity        │    │  Synchronization│
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Vault         │    │  Descriptor      │    │  Audit Chain    │
│   References    │    │  Metadata        │    │  (JSONL)        │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

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
│   ├── services.py        # Business logic
│   ├── forensic_timekeeper.py
│   ├── spice_descriptor_layer.py
│   └── ...
├── tests/                 # Test files
├── docs/                  # Documentation
├── examples/              # Usage examples
├── data/                  # Data files
├── logs/                  # Log files
├── Dockerfile             # Docker image
├── docker-compose.yml     # Docker services
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## API Endpoints

- `POST /processes` - Create process descriptor
- `GET /processes/{id}` - Retrieve process descriptor
- `GET /audit/{process_id}` - Get audit trail
- `GET /health` - System health check
- `GET /time/forensic` - Current forensic timestamp

## Configuration

Environment variables:

- `FORNSIC_TIME_ZONE` - Time zone for timestamps (default: UTC)
- `SPICE_DATA_PATH` - Path to SPICE descriptor data
- `LOG_LEVEL` - Logging level (default: INFO)

## Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_startup.py
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

This system is designed to comply with Article VII of the system constitution: "All memory is immutable and auditable." All operations generate immutable audit trails with cryptographic integrity guarantees.