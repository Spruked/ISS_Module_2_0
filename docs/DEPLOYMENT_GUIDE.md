# ISS Module v2 - Production Deployment Guide

## Overview

This guide provides comprehensive instructions for deploying the ISS Module v2 (Inventory Service System) with SPICE Descriptor Layer integration in production environments.

## Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional but recommended)
- 2GB RAM minimum
- 10GB storage minimum

## Quick Start

### Option 1: Direct Python Deployment

```bash
# Clone or copy the iss_module_v2 directory
cd iss_module_v2/

# Install dependencies
pip install -r requirements.txt

# Run the startup script
chmod +x startup.sh
./startup.sh
```

### Option 2: Docker Deployment

```bash
# Build and run with Docker Compose
cd iss_module_v2/
docker-compose up -d

# Check logs
docker-compose logs -f iss-module-v2
```

### Option 3: Kubernetes Deployment

```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/

# Check pod status
kubectl get pods -l app=iss-module-v2
```

## Configuration

### Environment Variables

Create a `.env` file in the iss_module_v2 directory:

```env
# Server Configuration
PORT=8000

# Forensic Time Configuration
NODE_ID=ISS_MODULE_V2
STORAGE_PATH=./forensic_logs

# SPICE Layer Configuration
SPICE_STORAGE_PATH=./spice_layer
MATRIX_ROOT=./memory_matrix

# API Configuration
API_TITLE=ISS Module v2 - Inventory Service System
API_DESCRIPTION=Forensic-grade inventory management with SPICE Descriptor Layer
API_VERSION=2.0.0

# Security
ALLOW_ORIGINS=*
SECRET_KEY=your-secret-key-here
```

## API Endpoints

Once deployed, the API will be available at `http://localhost:8000`

### Core Endpoints

- `GET /health` - System health check
- `GET /docs` - Interactive API documentation
- `GET /redoc` - Alternative API documentation

### Forensic Time Endpoints

- `GET /time/pulse` - Generate forensic timestamp
- `GET /time/verify` - Verify chain integrity
- `GET /time/history` - Get pulse history

### SPICE Descriptor Endpoints

- `POST /spice/descriptor` - Create process descriptor
- `GET /spice/descriptor/{id}` - Retrieve descriptor
- `GET /spice/find/glyph/{hash}` - Find by glyph reference
- `GET /spice/capability/report` - Process maturity report

### Audit Endpoints

- `GET /audit/trail/{id}` - Full audit reconstruction
- `GET /audit/verify/integrity` - System integrity check

## Data Storage

The system creates the following directory structure:

```
iss_module_v2/
├── forensic_logs/          # Forensic time data
│   ├── glyph_chain.jsonl   # Immutable pulse chain
│   └── forensic_audit.log  # Constitutional audit log
├── spice_layer/            # SPICE metadata layer
│   ├── spice_descriptors.jsonl  # Process descriptors
│   ├── spice_index.json          # O(1) lookup index
│   └── constitutional_binding.jsonl  # Article VII logs
└── memory_matrix/          # External vault references
    ├── apriori_vault.jsonl
    ├── aposteriori_vault.jsonl
    └── trace_vault.jsonl
```

## Monitoring

### Health Checks

The system provides comprehensive health monitoring:

```bash
# HTTP health check
curl http://localhost:8000/health

# Docker health check
docker ps
docker stats iss-module-v2
```

### Logs

```bash
# Application logs
docker-compose logs -f iss-module-v2

# Forensic audit logs
tail -f forensic_logs/forensic_audit.log

# SPICE constitutional logs
tail -f spice_layer/constitutional_binding.jsonl
```

## Security Considerations

### Constitutional Compliance

- **Article VII**: All memory immutable and auditable
- **Vault Contamination Prevention**: Read-only vault access
- **Non-Authoritative Design**: Advisory-only metadata

### Network Security

```bash
# Run behind reverse proxy (nginx recommended)
# Enable HTTPS in production
# Configure firewall rules
# Use secrets management for sensitive data
```

## Scaling

### Horizontal Scaling

```yaml
# docker-compose.yml for multiple instances
services:
  iss-module-v2:
    deploy:
      replicas: 3
    volumes:
      - shared_logs:/app/forensic_logs
      - shared_spice:/app/spice_layer
```

### Load Balancing

```nginx
# nginx.conf
upstream iss_module_v2 {
    server iss-module-v2-1:8000;
    server iss-module-v2-2:8000;
    server iss-module-v2-3:8000;
}
```

## Backup and Recovery

### Automated Backups

```bash
#!/bin/bash
# backup.sh
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
tar -czf backup_$TIMESTAMP.tar.gz \
    forensic_logs/ \
    spice_layer/ \
    memory_matrix/
```

### Recovery Procedure

```bash
# Stop the service
docker-compose down

# Restore from backup
tar -xzf backup_latest.tar.gz

# Restart the service
docker-compose up -d
```

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change port in .env
   PORT=8001
   ```

2. **Permission denied**
   ```bash
   # Fix directory permissions
   chown -R 1000:1000 forensic_logs/ spice_layer/
   ```

3. **Memory issues**
   ```bash
   # Increase Docker memory limit
   docker-compose.yml -> deploy.resources.limits.memory: 4G
   ```

### Debug Mode

```bash
# Run with debug logging
docker-compose up -d
docker-compose logs -f --tail=100 iss-module-v2
```

## Integration Examples

### Worker SKG Integration

```python
import requests

# Create process descriptor
response = requests.post("http://localhost:8000/spice/descriptor", json={
    "process_name": "WorkerSKG_Job_Execution",
    "process_version": "2.1.0",
    "capability_level": 4,
    "process_outcome": "compliant",
    "compliance_score": 0.94,
    "apriori_refs": ["constraint:deterministic_replay"],
    "aposteriori_refs": ["outcome:job_success"],
    "glyph_range_start": "a1b2c3d4",
    "glyph_range_end": "e5f6g7h8",
    "glyph_count": 42,
    "evidence_required": ["job_input", "execution_log"],
    "evidence_provided": ["job_output", "forensic_timestamp"],
    "assessed_by": "WorkerSKG_Audit",
    "assessment_method": "automated_verification",
    "active_constraints": ["immutable_memory"]
})

print(f"Created descriptor: {response.json()['descriptor_id']}")
```

## Support

For issues and questions:
- Check the logs: `docker-compose logs iss-module-v2`
- Run diagnostics: `python debug_harness.py`
- Review API docs: `http://localhost:8000/docs`

## Version History

- **v2.0.0**: Initial production release
  - FastAPI implementation
  - SPICE Descriptor Layer integration
  - Constitutional Article VII compliance
  - Docker containerization
  - Comprehensive audit trails