# Forensic Time Plugin Module
## Constitutional-Grade Timekeeping with Glyph Trace Logic

**Article VII Compliance**: All memory is immutable and auditable.

---

## Overview

This plugin module provides forensic-grade timestamping for any system requiring:
- **Space-time compliance** (survives real space travel)
- **Glyph trace logic** (immutable blockchain-style chain)
- **Forensic auditability** (cryptographic integrity verification)
- **Dashboard integration** (real-time visualization)

---

## What to Store in Every ISS Pulse (Minimal, Correct)

```json
{
  "tai_ns": 523091057084,
  "utc_iso": "2026-02-13T04:54:25.008460+00:00",
  "et_s": 824230534.1924601,
  "utc_unix": 1770958465.00846,
  "epoch_days": 9539.704456116435,
  "julian_date": 2461084.7044561165,
  "pulse_id": "9bb07db01cdad887fac40520ff4e1965",
  "glyph_hash": "e1a39142ac80cd4b16fc4eed31a6ba9359802c22c0d201ea916be99d17704d2c",
  "chain_hash": "07341f93f817e4017fb199c6c5313941",
  "source_node": "CALEON_PRIME_ISS"
}
```

### Time Domains Explained

| Field | Purpose | Use Case |
|-------|---------|----------|
| `tai_ns` | Integer nanoseconds since epoch | Monotonic truth, never jumps |
| `utc_iso` | ISO 8601 timestamp | Human display, leap-second aware |
| `et_s` | Seconds past J2000 (TDB/ET) | SPICE/ephemeris calculations |
| `utc_unix` | Unix timestamp | System compatibility |
| `epoch_days` | Days since J2000 | Orbital mechanics |
| `julian_date` | Julian Date | Astronomical reference |

---

## Installation

```bash
pip install forensic-time-plugin
```

Or copy `forensic_time_plugin.py` to your project.

---

## Quick Start

```python
from forensic_time_plugin import ForensicTimePlugin, ForensicConfig

# Initialize plugin
plugin = ForensicTimePlugin(ForensicConfig(
    node_id="ISS_MODULE_ALPHA",
    storage_path="./forensic_logs"
))

# Generate forensic pulse
pulse = plugin.pulse()
print(f"TAI: {pulse['tai_ns']}")
print(f"UTC: {pulse['utc_iso']}")
print(f"ET:  {pulse['et_s']}")

# Verify chain integrity
report = plugin.verify()
assert report['integrity'], "Chain violation detected!"
```

---

## Dashboard Integration

### Standalone HTML Dashboard

Open `forensic_time_dashboard.html` in any browser:

```bash
python -m http.server 8000
# Navigate to http://localhost:8000/forensic_time_dashboard.html
```

### Embed in Existing Dashboard

```python
from forensic_time_plugin import ForensicDashboardWidget

widget = ForensicDashboardWidget(plugin)
component_data = widget.render_component()
# Integrate component_data into your dashboard framework
```

---

## System Integrations

### FastAPI (ISS Module)

```python
from fastapi import FastAPI
from forensic_time_plugin import ForensicTimePlugin

app = FastAPI()
plugin = ForensicTimePlugin()

@app.get("/time/pulse")
async def get_pulse():
    return plugin.pulse()

@app.get("/time/verify")
async def verify():
    return plugin.verify()
```

### Worker SKG

```python
class ForensicWorker:
    def __init__(self):
        self.time_plugin = ForensicTimePlugin()
    
    def execute(self, job):
        start = self.time_plugin.pulse()
        # ... execute job ...
        end = self.time_plugin.pulse()
        return {
            "result": result,
            "forensic_trace": {
                "start": start['pulse_id'],
                "end": end['pulse_id']
            }
        }
```

### CALI ORB

```python
class CALIForensicBridge:
    def __init__(self):
        self.plugin = ForensicTimePlugin(
            ForensicConfig(node_id="CALI_ORB")
        )
    
    def log_cognition(self, thought):
        pulse = self.plugin.pulse()
        # Append to cali_immutable_matrix
```

---

## Glyph Trace Logic

Every pulse generates:

1. **Pulse ID**: SHA256 hash of content
2. **Glyph Hash**: Full cryptographic signature
3. **Chain Hash**: Links to previous pulse (immutable chain)

### Chain Integrity Verification

```python
report = plugin.verify()
# Returns:
# {
#   "status": "CLEAN" | "VIOLATED",
#   "integrity": true | false,
#   "violations": [...],
#   "pulses": 1000
# }
```

---

## Constitutional Compliance

**Article VII - Flow Invariants**:
- All memory is **immutable**
- All memory is **auditable**
- No retroactive modifications
- Cryptographic chain of custody

---

## File Structure

```
forensic_logs/
├── glyph_chain.jsonl      # Immutable pulse chain
├── forensic_audit.log     # Constitutional binding logs
└── dashboard.html         # Visualization (optional)
```

---

## API Reference

### `ForensicTimePlugin(config)`

Initialize plugin with configuration.

### `pulse() -> dict`

Generate new forensic time pulse.

### `verify() -> dict`

Verify entire chain integrity.

### `get_chain(limit=100) -> list`

Retrieve pulse history.

### `export_dashboard(path, refresh_ms=1000)`

Export standalone HTML dashboard.

---

## Space-Time Survivability

This system survives real space travel by providing:

- **TAI**: Monotonic time (no leap seconds)
- **UTC**: Earth reference (leap-second aware)
- **ET**: Space time (independent of Earth rotation)

---

## License

Constitutional Law Article VII - Immutable and Auditable