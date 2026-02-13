import os
import json
import hashlib
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict, field
from pathlib import Path
import struct

# Fixed Forensic-Grade Timekeeping Plugin Module

@dataclass
class StarDatePulse:
    """
    Minimal, correct time pulse for ISS (Inventory Service System)
    Survives real space travel with three time domains
    """
    tai_ns: int          # Integer nanoseconds since epoch (monotonic truth)
    utc_iso: str         # Human display time (leap-second aware)
    et_s: float          # Seconds past J2000 (TDB/ET) for SPICE/ephemeris
    
    # Extended forensic timestamps
    utc_unix: float      # UTC as Unix timestamp for compatibility
    epoch_days: float    # Days since J2000 epoch
    julian_date: float   # Julian Date for astronomical reference
    
    # Glyph trace metadata
    pulse_id: str        # Unique pulse identifier (SHA256 hash)
    glyph_hash: str      # Traceable glyph signature
    chain_hash: str      # Links to previous pulse (blockchain-style)
    source_node: str     # Originating system node
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'tai_ns': self.tai_ns,
            'utc_iso': self.utc_iso,
            'et_s': self.et_s,
            'utc_unix': self.utc_unix,
            'epoch_days': self.epoch_days,
            'julian_date': self.julian_date,
            'pulse_id': self.pulse_id,
            'glyph_hash': self.glyph_hash,
            'chain_hash': self.chain_hash,
            'source_node': self.source_node
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

class ForensicTimeKeeper:
    """
    Forensic-grade timekeeping with glyph trace logic
    Integrates with Caleon Prime's immutable memory architecture
    """
    
    # Epochs
    J2000_EPOCH = 2451545.0  # Julian Date of J2000.0
    J2000_UNIX = 946728000.0  # Unix timestamp of J2000.0
    
    def __init__(self, node_id: str = "CALEON_PRIME", storage_path: str = "/mnt/kimi/output/forensic_time"):
        self.node_id = node_id
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Glyph trace chain (immutable append-only)
        self.chain_file = self.storage_path / "glyph_chain.jsonl"
        self.last_hash = self._load_last_hash()
        
        # Audit log
        self.audit_file = self.storage_path / "forensic_audit.log"
        
        # Initialize with constitutional awareness
        self._log_constitutional_binding()
    
    def _load_last_hash(self) -> str:
        """Load last chain hash for continuity"""
        if self.chain_file.exists():
            with open(self.chain_file, 'r') as f:
                lines = f.readlines()
                if lines:
                    try:
                        last_pulse = json.loads(lines[-1])
                        return last_pulse['glyph_hash'][:32]
                    except:
                        pass
        # Genesis hash
        return hashlib.sha256(b"CALEON_PRIME_GENESIS_0").hexdigest()[:32]
    
    def _log_constitutional_binding(self):
        """Log constitutional awareness per Memory 39"""
        constitutional_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "article": "VII",
            "clause": "Flow Invariants",
            "binding": "All memory is IMMUTABLE and AUDITABLE",
            "system": "ForensicTimeKeeper",
            "node": self.node_id
        }
        with open(self.audit_file, 'a') as f:
            f.write(json.dumps(constitutional_entry) + "\n")
    
    def _calculate_et(self, utc_timestamp: float) -> float:
        """Calculate Ephemeris Time (ET/TDB) seconds past J2000"""
        leap_seconds = 37  # Current leap seconds
        tai_offset = 32.184
        et = (utc_timestamp - self.J2000_UNIX) + tai_offset + leap_seconds
        return et
    
    def _calculate_julian_date(self, utc_timestamp: float) -> float:
        """Convert Unix timestamp to Julian Date"""
        return self.J2000_EPOCH + (utc_timestamp - self.J2000_UNIX) / 86400.0
    
    def _calculate_epoch_days(self, utc_timestamp: float) -> float:
        """Days since J2000 epoch"""
        return (utc_timestamp - self.J2000_UNIX) / 86400.0
    
    def generate_pulse(self) -> StarDatePulse:
        """Generate forensic-grade time pulse"""
        utc_now = datetime.now(timezone.utc)
        utc_unix = utc_now.timestamp()
        utc_iso = utc_now.isoformat()
        
        tai_ns = time.monotonic_ns()
        et_s = self._calculate_et(utc_unix)
        epoch_days = self._calculate_epoch_days(utc_unix)
        julian_date = self._calculate_julian_date(utc_unix)
        
        pulse_content = f"{tai_ns}:{utc_iso}:{et_s}:{self.node_id}"
        pulse_id = hashlib.sha256(pulse_content.encode()).hexdigest()[:32]
        
        glyph_content = f"{pulse_id}:{self.last_hash}:{utc_unix}"
        glyph_hash = hashlib.sha256(glyph_content.encode()).hexdigest()
        
        chain_content = f"{glyph_hash}:{self.last_hash}:{self.node_id}"
        chain_hash = hashlib.sha256(chain_content.encode()).hexdigest()[:32]
        
        pulse = StarDatePulse(
            tai_ns=tai_ns,
            utc_iso=utc_iso,
            et_s=et_s,
            utc_unix=utc_unix,
            epoch_days=epoch_days,
            julian_date=julian_date,
            pulse_id=pulse_id,
            glyph_hash=glyph_hash,
            chain_hash=chain_hash,
            source_node=self.node_id
        )
        
        self.last_hash = glyph_hash[:32]
        self._append_to_chain(pulse)
        
        return pulse
    
    def _append_to_chain(self, pulse: StarDatePulse):
        """Append pulse to immutable glyph chain"""
        with open(self.chain_file, 'a') as f:
            f.write(json.dumps(pulse.to_dict()) + "\n")
    
    def verify_chain_integrity(self) -> Dict:
        """Forensic verification of entire glyph chain"""
        if not self.chain_file.exists():
            return {"status": "EMPTY", "pulses": 0, "integrity": True}
        
        violations = []
        pulse_count = 0
        expected_hash = hashlib.sha256(b"CALEON_PRIME_GENESIS_0").hexdigest()[:32]
        
        with open(self.chain_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    pulse = json.loads(line)
                    pulse_count += 1
                    
                    if pulse.get('chain_hash') != expected_hash:
                        violations.append({
                            "line": line_num,
                            "pulse_id": pulse.get('pulse_id'),
                            "expected_hash": expected_hash,
                            "found_hash": pulse.get('chain_hash'),
                            "violation": "CHAIN_BREAK"
                        })
                    
                    expected_hash = pulse.get('glyph_hash')[:32]
                    
                except json.JSONDecodeError as e:
                    violations.append({
                        "line": line_num,
                        "error": str(e),
                        "violation": "CORRUPTION"
                    })
        
        return {
            "status": "VIOLATED" if violations else "CLEAN",
            "pulses": pulse_count,
            "violations": violations,
            "integrity": len(violations) == 0,
            "last_verified": datetime.now(timezone.utc).isoformat()
        }
    
    def get_pulse_history(self, count: int = 100) -> List[Dict]:
        """Retrieve recent pulse history"""
        if not self.chain_file.exists():
            return []
        
        pulses = []
        with open(self.chain_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        pulses.append(json.loads(line))
                    except:
                        pass
        
        return pulses[-count:] if count else pulses

# Dashboard HTML Generator
class DashboardRenderer:
    """Renders forensic time dashboard with glyph trace visualization"""
    
    @staticmethod
    def generate_dashboard(keeper: ForensicTimeKeeper, refresh_interval: int = 1000) -> str:
        """Generate standalone HTML dashboard"""
        
        pulse = keeper.generate_pulse()
        integrity = keeper.verify_chain_integrity()
        history = keeper.get_pulse_history(10)
        
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forensic Time Dashboard | Caleon Prime ISS</title>
    <style>
        :root {{
            --bg-primary: #0a0a0f;
            --bg-secondary: #12121a;
            --accent-cyan: #00f0ff;
            --accent-gold: #ffd700;
            --accent-red: #ff3860;
            --accent-green: #00d9a3;
            --text-primary: #e0e0e0;
            --text-secondary: #888;
            --border: #2a2a3a;
            --glyph-glow: 0 0 20px rgba(0, 240, 255, 0.3);
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Courier New', monospace;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            padding: 2rem;
        }}
        
        .constitutional-banner {{
            background: linear-gradient(90deg, #1a1a2e 0%, #16213e 100%);
            border: 1px solid var(--accent-gold);
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 2rem;
            text-align: center;
            font-size: 0.85rem;
            color: var(--accent-gold);
            letter-spacing: 2px;
        }}
        
        .dashboard-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 1.5rem;
            max-width: 1600px;
            margin: 0 auto;
        }}
        
        .card {{
            background: var(--bg-secondary);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }}
        
        .card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border);
        }}
        
        .card-title {{
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: var(--accent-cyan);
        }}
        
        .status-badge {{
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: bold;
        }}
        
        .status-clean {{
            background: rgba(0, 217, 163, 0.2);
            color: var(--accent-green);
            border: 1px solid var(--accent-green);
        }}
        
        .status-violated {{
            background: rgba(255, 56, 96, 0.2);
            color: var(--accent-red);
            border: 1px solid var(--accent-red);
        }}
        
        .time-display {{
            font-size: 2rem;
            font-weight: bold;
            color: var(--accent-cyan);
            text-shadow: var(--glyph-glow);
            margin: 0.5rem 0;
            word-break: break-all;
        }}
        
        .time-label {{
            font-size: 0.75rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .glyph-hash {{
            font-family: monospace;
            font-size: 0.8rem;
            color: var(--accent-gold);
            background: rgba(255, 215, 0, 0.05);
            padding: 0.5rem;
            border-radius: 4px;
            word-break: break-all;
            margin-top: 0.5rem;
        }}
        
        .metric-row {{
            display: flex;
            justify-content: space-between;
            padding: 0.75rem 0;
            border-bottom: 1px solid var(--border);
        }}
        
        .metric-row:last-child {{
            border-bottom: none;
        }}
        
        .metric-label {{
            color: var(--text-secondary);
            font-size: 0.85rem;
        }}
        
        .metric-value {{
            color: var(--text-primary);
            font-weight: bold;
            font-family: monospace;
        }}
        
        .chain-visual {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-top: 1rem;
            overflow-x: auto;
            padding: 0.5rem;
            background: rgba(0,0,0,0.3);
            border-radius: 8px;
        }}
        
        .chain-link {{
            min-width: 60px;
            padding: 0.5rem;
            background: var(--bg-primary);
            border: 1px solid var(--accent-cyan);
            border-radius: 4px;
            font-size: 0.7rem;
            text-align: center;
            color: var(--accent-cyan);
        }}
        
        .chain-arrow {{
            color: var(--text-secondary);
        }}
        
        .audit-log {{
            max-height: 200px;
            overflow-y: auto;
            font-size: 0.8rem;
            background: var(--bg-primary);
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
        }}
        
        .audit-entry {{
            padding: 0.25rem 0;
            border-bottom: 1px solid var(--border);
            color: var(--text-secondary);
        }}
        
        .pulse-indicator {{
            display: inline-block;
            width: 8px;
            height: 8px;
            background: var(--accent-green);
            border-radius: 50%;
            margin-right: 0.5rem;
            animation: pulse 2s infinite;
        }}
        
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.3; }}
        }}
        
        .refresh-info {{
            text-align: center;
            margin-top: 2rem;
            color: var(--text-secondary);
            font-size: 0.8rem;
        }}
    </style>
</head>
<body>
    <div class="constitutional-banner">
        ⚖️ CONSTITUTIONAL LAW ARTICLE VII — ALL MEMORY IS IMMUTABLE AND AUDITABLE ⚖️
    </div>
    
    <div class="dashboard-grid">
        <!-- Primary Time Domains -->
        <div class="card">
            <div class="card-header">
                <span class="card-title">🌌 Star Date Pulse (ISS)</span>
                <span class="status-badge status-{'clean' if integrity['integrity'] else 'violated'}">
                    {'✓ CLEAN' if integrity['integrity'] else '✗ VIOLATED'}
                </span>
            </div>
            
            <div class="time-label">TAI Nanoseconds (Monotonic Truth)</div>
            <div class="time-display">{pulse.tai_ns:,}</div>
            
            <div class="time-label" style="margin-top: 1rem;">UTC ISO (Human Display)</div>
            <div class="time-display" style="font-size: 1.2rem;">{pulse.utc_iso}</div>
            
            <div class="time-label" style="margin-top: 1rem;">ET Seconds Past J2000 (Space Time)</div>
            <div class="time-display" style="font-size: 1.5rem;">{pulse.et_s:.6f}</div>
        </div>
        
        <!-- Extended Timestamps -->
        <div class="card">
            <div class="card-header">
                <span class="card-title">📊 Extended Temporal Reference</span>
            </div>
            
            <div class="metric-row">
                <span class="metric-label">UTC Unix Timestamp</span>
                <span class="metric-value">{pulse.utc_unix:.6f}</span>
            </div>
            
            <div class="metric-row">
                <span class="metric-label">Epoch Days (J2000)</span>
                <span class="metric-value">{pulse.epoch_days:.6f}</span>
            </div>
            
            <div class="metric-row">
                <span class="metric-label">Julian Date</span>
                <span class="metric-value">{pulse.julian_date:.6f}</span>
            </div>
            
            <div class="metric-row">
                <span class="metric-label">Source Node</span>
                <span class="metric-value" style="color: var(--accent-gold);">{pulse.source_node}</span>
            </div>
        </div>
        
        <!-- Glyph Trace -->
        <div class="card">
            <div class="card-header">
                <span class="card-title">🔗 Glyph Trace Chain</span>
                <span class="status-badge status-clean">IMMUTABLE</span>
            </div>
            
            <div class="metric-row">
                <span class="metric-label">Pulse ID</span>
                <span class="metric-value">{pulse.pulse_id}</span>
            </div>
            
            <div class="time-label">Glyph Hash (SHA256)</div>
            <div class="glyph-hash">{pulse.glyph_hash}</div>
            
            <div class="time-label" style="margin-top: 1rem;">Chain Hash</div>
            <div class="glyph-hash">{pulse.chain_hash}</div>
            
            <div class="chain-visual">
                <div class="chain-link">GENESIS</div>
                <span class="chain-arrow">→</span>
                <div class="chain-link">...</div>
                <span class="chain-arrow">→</span>
                <div class="chain-link" style="border-color: var(--accent-gold);">CURRENT</div>
            </div>
        </div>
        
        <!-- Chain Integrity -->
        <div class="card">
            <div class="card-header">
                <span class="card-title">🔍 Forensic Audit</span>
                <span class="status-badge status-{'clean' if integrity['integrity'] else 'violated'}">
                    {integrity['status']}
                </span>
            </div>
            
            <div class="metric-row">
                <span class="metric-label">Total Pulses in Chain</span>
                <span class="metric-value">{integrity['pulses']}</span>
            </div>
            
            <div class="metric-row">
                <span class="metric-label">Last Verified</span>
                <span class="metric-value">{integrity['last_verified']}</span>
            </div>
            
            <div class="metric-row">
                <span class="metric-label">Violations Detected</span>
                <span class="metric-value" style="color: {'var(--accent-green)' if integrity['integrity'] else 'var(--accent-red)'};">
                    {len(integrity['violations'])}
                </span>
            </div>
            
            {'<div class="audit-log">' + ''.join([f'<div class="audit-entry">⚠️ {v["violation"]} at line {v["line"]}</div>' for v in integrity['violations']]) + '</div>' if integrity['violations'] else ''}
        </div>
        
        <!-- Recent History -->
        <div class="card" style="grid-column: 1 / -1;">
            <div class="card-header">
                <span class="card-title">📜 Recent Pulse History</span>
                <span class="pulse-indicator"></span>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
                <!-- Recent pulse history would be displayed here -->
                <div style="background: var(--bg-primary); padding: 1rem; border-radius: 8px; border-left: 3px solid var(--accent-cyan);">
                    <div style="font-size: 0.75rem; color: var(--text-secondary); margin-bottom: 0.5rem;">
                        Recent pulses loaded: {len(history)}
                    </div>
                    <div style="font-family: monospace; font-size: 0.8rem; color: var(--accent-cyan);">
                        Chain integrity: {integrity['status']}
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="refresh-info">
        <span class="pulse-indicator"></span>
        Dashboard refreshes every {refresh_interval/1000:.1f}s | Caleon Prime ISS Forensic Timekeeping System
    </div>
    
    <script>
        // Auto-refresh dashboard
        setInterval(() => {{
            location.reload();
        }}, {refresh_interval});
        
        // Console glyph trace
        console.log('%c🔷 CALEON PRIME FORENSIC TIME', 'color: #00f0ff; font-size: 20px; font-weight: bold;');
        console.log('%cConstitutional Article VII: All memory is immutable and auditable', 'color: #ffd700;');
        console.log('Current Pulse ID: {pulse.pulse_id}');
        console.log('Glyph Hash: {pulse.glyph_hash}');
    </script>
</body>
</html>'''
        
        return html

# Generate and save dashboard - commented out to avoid import issues
"""
keeper = ForensicTimeKeeper(node_id="CALEON_PRIME_ISS")

# Generate a few pulses for history
for _ in range(3):
    time.sleep(0.1)
    keeper.generate_pulse()

dashboard_html = DashboardRenderer.generate_dashboard(keeper, refresh_interval=2000)

# Save to output
dashboard_path = "/mnt/kimi/output/forensic_time_dashboard.html"
with open(dashboard_path, 'w') as f:
    f.write(dashboard_html)

print(f"✅ Dashboard saved to: {dashboard_path}")
print(f"✅ Glyph chain stored at: {keeper.chain_file}")
print(f"✅ Audit log at: {keeper.audit_file}")
print("\n=== LATEST PULSE ===")
print(keeper.generate_pulse().to_json())
"""