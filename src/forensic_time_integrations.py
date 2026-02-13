"""
FORENSIC TIME INTEGRATION EXAMPLES
==================================
Examples of integrating the ForensicTimePlugin with various systems.

Constitutional Compliance: Article VII - All memory is immutable and auditable
"""

import json
import asyncio
from typing import Dict, List
from datetime import datetime, timezone
from pathlib import Path

# Import the plugin (in real usage, this would be from .forensic_time_plugin import ...)
from .forensic_time_plugin import ForensicTimePlugin, ForensicConfig

# =============================================================================
# EXAMPLE 1: FASTAPI ENDPOINT INTEGRATION
# =============================================================================

fastapi_example = '''
"""
FastAPI Integration Example
Add this to your FastAPI application for time pulse endpoints
"""

from fastapi import FastAPI, HTTPException
from .forensic_time_plugin import ForensicTimePlugin, ForensicConfig

app = FastAPI(title="ISS Time Service", version="1.0.0")

# Initialize forensic time plugin
time_plugin = ForensicTimePlugin(ForensicConfig(
    node_id="ISS_FASTAPI_MODULE",
    storage_path="./forensic_logs"
))

@app.get("/time/pulse")
async def get_time_pulse():
    """Get current forensic time pulse"""
    try:
        pulse = time_plugin.pulse()
        return {
            "status": "success",
            "pulse": pulse,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/time/verify")
async def verify_chain_integrity():
    """Verify glyph chain integrity"""
    try:
        report = time_plugin.verify()
        return {
            "status": "success",
            "integrity_report": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/time/history")
async def get_pulse_history(limit: int = 100):
    """Get pulse history"""
    try:
        history = time_plugin.get_chain(limit)
        return {
            "status": "success",
            "history": history,
            "count": len(history)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Usage: uvicorn this_module:app --reload
'''

# =============================================================================
# EXAMPLE 2: WORKER SKG JOB EXECUTION TRACING
# =============================================================================

worker_skg_example = '''
"""
Worker SKG Integration Example
Add forensic timestamping to job execution
"""

import time
from typing import Any, Dict
from .forensic_time_plugin import ForensicTimePlugin, ForensicConfig

class TracedWorkerSKG:
    """Worker SKG with forensic time tracing"""

    def __init__(self, node_id: str = "WORKER_SKG_NODE"):
        self.time_plugin = ForensicTimePlugin(ForensicConfig(
            node_id=node_id,
            storage_path="./worker_logs"
        ))

    def execute_job(self, job_id: str, job_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute job with full forensic tracing"""

        # Pre-execution pulse
        pre_pulse = self.time_plugin.pulse()
        start_time = time.time()

        try:
            # Job execution logic here
            result = self._process_job(job_data)

            # Post-execution pulse
            post_pulse = self.time_plugin.pulse()
            end_time = time.time()

            # Create traced job record
            traced_job = {
                "job_id": job_id,
                "execution_trace": {
                    "pre_pulse": pre_pulse,
                    "post_pulse": post_pulse,
                    "execution_time": end_time - start_time,
                    "glyph_range": f"{pre_pulse['glyph_hash'][:16]}...{post_pulse['glyph_hash'][:16]}"
                },
                "result": result,
                "status": "completed"
            }

            return traced_job

        except Exception as e:
            # Error pulse
            error_pulse = self.time_plugin.pulse()

            return {
                "job_id": job_id,
                "status": "failed",
                "error": str(e),
                "error_pulse": error_pulse
            }

    def _process_job(self, job_data: Dict[str, Any]) -> Dict[str, Any]:
        """Mock job processing"""
        time.sleep(0.1)  # Simulate work
        return {"processed": True, "data": job_data}

# Usage example
worker = TracedWorkerSKG("WORKER_SKG_001")
result = worker.execute_job("job_123", {"input": "test_data"})
print(f"Job completed with trace: {result['execution_trace']['glyph_range']}")
'''

# =============================================================================
# EXAMPLE 3: CALI ORB COGNITIVE EVENT LOGGING
# =============================================================================

cali_orb_example = '''
"""
CALI ORB Integration Example
Log cognitive events with forensic timestamps
"""

from enum import Enum
from .forensic_time_plugin import ForensicTimePlugin, ForensicConfig

class CognitiveEvent(Enum):
    PERCEPTION = "perception"
    REASONING = "reasoning"
    DECISION = "decision"
    ACTION = "action"
    LEARNING = "learning"

class CALIOrbLogger:
    """CALI ORB with forensic event logging"""

    def __init__(self, orb_id: str = "CALI_ORB_001"):
        self.time_plugin = ForensicTimePlugin(ForensicConfig(
            node_id=orb_id,
            storage_path="./cali_logs"
        ))
        self.event_log = []

    def log_cognitive_event(self,
                          event_type: CognitiveEvent,
                          description: str,
                          context: Dict = None) -> Dict:
        """Log cognitive event with forensic timestamp"""

        pulse = self.time_plugin.pulse()

        event = {
            "event_id": f"{event_type.value}_{pulse['pulse_id'][:16]}",
            "event_type": event_type.value,
            "description": description,
            "context": context or {},
            "forensic_pulse": pulse,
            "logged_at": pulse['utc_iso']
        }

        self.event_log.append(event)

        # Also log to separate cognitive audit file
        self._audit_cognitive_event(event)

        return event

    def _audit_cognitive_event(self, event: Dict):
        """Audit cognitive event to immutable log"""
        audit_path = Path("./cali_logs/cognitive_audit.jsonl")
        audit_path.parent.mkdir(parents=True, exist_ok=True)

        with open(audit_path, 'a') as f:
            f.write(json.dumps(event) + "\\n")

    def get_cognitive_history(self, event_type: CognitiveEvent = None) -> List[Dict]:
        """Retrieve cognitive event history"""
        if event_type:
            return [e for e in self.event_log if e['event_type'] == event_type.value]
        return self.event_log

# Usage example
orb = CALIOrbLogger("CALI_ORB_ALPHA")
event = orb.log_cognitive_event(
    CognitiveEvent.DECISION,
    "Selected optimal trajectory",
    {"confidence": 0.94, "alternatives": 3}
)
print(f"Logged cognitive event: {event['event_id']}")
'''

# =============================================================================
# EXAMPLE 4: DALS ACTION TIMESTAMPING
# =============================================================================

dals_example = '''
"""
DALS Integration Example
Timestamp all actions in the DALS system
"""

from typing import List, Optional
from .forensic_time_plugin import ForensicTimePlugin, ForensicConfig

class DALSActionLogger:
    """DALS with forensic action timestamping"""

    def __init__(self, dals_node: str = "DALS_NODE_001"):
        self.time_plugin = ForensicTimePlugin(ForensicConfig(
            node_id=dals_node,
            storage_path="./dals_logs"
        ))
        self.active_actions = {}

    def start_action(self,
                    action_id: str,
                    action_type: str,
                    parameters: Dict = None) -> Dict:
        """Start an action with forensic timestamp"""

        pulse = self.time_plugin.pulse()

        action_record = {
            "action_id": action_id,
            "action_type": action_type,
            "parameters": parameters or {},
            "start_pulse": pulse,
            "status": "running",
            "glyph_start": pulse['glyph_hash']
        }

        self.active_actions[action_id] = action_record

        # Log to DALS audit
        self._log_action_event(action_record, "STARTED")

        return action_record

    def complete_action(self, action_id: str, result: Dict = None) -> Optional[Dict]:
        """Complete an action with end timestamp"""

        if action_id not in self.active_actions:
            return None

        pulse = self.time_plugin.pulse()

        action_record = self.active_actions[action_id]
        action_record.update({
            "end_pulse": pulse,
            "result": result or {},
            "status": "completed",
            "glyph_end": pulse['glyph_hash'],
            "glyph_range": f"{action_record['glyph_start'][:16]}...{pulse['glyph_hash'][:16]}"
        })

        # Log completion
        self._log_action_event(action_record, "COMPLETED")

        del self.active_actions[action_id]
        return action_record

    def _log_action_event(self, action_record: Dict, event_type: str):
        """Log action event to audit trail"""
        audit_path = Path("./dals_logs/action_audit.jsonl")
        audit_path.parent.mkdir(parents=True, exist_ok=True)

        audit_entry = {
            "event_type": event_type,
            "action_record": action_record,
            "logged_at": datetime.now(timezone.utc).isoformat()
        }

        with open(audit_path, 'a') as f:
            f.write(json.dumps(audit_entry) + "\\n")

# Usage example
dals = DALSActionLogger("DALS_NAVIGATION")
action = dals.start_action("nav_001", "trajectory_calculation", {"destination": "L2"})
# ... action processing ...
result = dals.complete_action("nav_001", {"trajectory": "calculated", "duration": 2.3})
print(f"Action completed with glyph range: {result['glyph_range']}")
'''

# =============================================================================
# EXAMPLE 5: DASHBOARD WIDGET INTEGRATION
# =============================================================================

dashboard_widget_example = '''
"""
Dashboard Widget Integration Example
Add forensic time widget to any dashboard
"""

import json
from .forensic_time_plugin import ForensicTimePlugin, ForensicConfig

class ForensicTimeWidget:
    """Dashboard widget for forensic time display"""

    def __init__(self, plugin: ForensicTimePlugin):
        self.plugin = plugin

    def render_widget_html(self) -> str:
        """Render HTML widget for dashboard integration"""

        pulse = self.plugin.pulse()
        integrity = self.plugin.verify()

        html = f"""
        <div class="forensic-time-widget" style="
            border: 1px solid #00f0ff;
            border-radius: 8px;
            padding: 1rem;
            background: #0a0a0f;
            color: #e0e0e0;
            font-family: monospace;
            font-size: 0.8rem;
        ">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                <span style="color: #00f0ff; font-weight: bold;">🔷 FORENSIC TIME</span>
                <span style="color: {'#00d9a3' if integrity['integrity'] else '#ff3860'};">
                    {'✓' if integrity['integrity'] else '✗'}
                </span>
            </div>

            <div style="margin-bottom: 0.5rem;">
                <div style="color: #888; font-size: 0.7rem;">TAI NS</div>
                <div style="color: #00f0ff; font-size: 1.2rem;">{pulse['tai_ns']:,}</div>
            </div>

            <div style="margin-bottom: 0.5rem;">
                <div style="color: #888; font-size: 0.7rem;">UTC ISO</div>
                <div style="color: #ffd700;">{pulse['utc_iso']}</div>
            </div>

            <div style="margin-bottom: 0.5rem;">
                <div style="color: #888; font-size: 0.7rem;">ET S (J2000)</div>
                <div style="color: #e0e0e0;">{pulse['et_s']:.6f}</div>
            </div>

            <div style="font-size: 0.6rem; color: #ffd700; word-break: break-all;">
                {pulse['glyph_hash'][:32]}...
            </div>
        </div>
        """

        return html

    def get_widget_data(self) -> Dict:
        """Get widget data for AJAX updates"""
        pulse = self.plugin.pulse()
        integrity = self.plugin.verify()

        return {
            "pulse": pulse,
            "integrity": integrity,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

# Usage in dashboard
plugin = ForensicTimePlugin(ForensicConfig(node_id="DASHBOARD_WIDGET"))
widget = ForensicTimeWidget(plugin)

# Get HTML for embedding
html_widget = widget.render_widget_html()
print("Widget HTML generated for dashboard integration")
'''

# =============================================================================
# MAIN DEMO FUNCTION
# =============================================================================

def run_integration_demos():
    """Run all integration examples"""

    print("=" * 80)
    print("FORENSIC TIME INTEGRATION EXAMPLES")
    print("Constitutional Article VII: All memory is immutable and auditable")
    print("=" * 80)

    # Demo 1: Basic plugin usage
    print("\\n1. BASIC PLUGIN USAGE")
    print("-" * 40)

    plugin = ForensicTimePlugin(ForensicConfig(
        node_id="INTEGRATION_DEMO",
        storage_path="./demo_logs"
    ))

    pulse = plugin.pulse()
    print(f"Generated pulse: {pulse['pulse_id']}")
    print(f"TAI: {pulse['tai_ns']:,}")
    print(f"UTC: {pulse['utc_iso']}")
    print(f"ET: {pulse['et_s']:.6f}")

    # Demo 2: Integrity verification
    print("\\n2. INTEGRITY VERIFICATION")
    print("-" * 40)

    report = plugin.verify()
    print(f"Chain status: {report['status']}")
    print(f"Pulses: {report['pulses']}")
    print(f"Integrity: {report['integrity']}")

    # Demo 3: FastAPI endpoint simulation
    print("\\n3. FASTAPI ENDPOINT SIMULATION")
    print("-" * 40)

    # Simulate API call
    api_pulse = plugin.pulse()
    print(f"API Pulse: {api_pulse['pulse_id']}")

    print("\\n" + "=" * 80)
    print("INTEGRATION EXAMPLES READY FOR DEPLOYMENT")
    print("=" * 80)

if __name__ == "__main__":
    run_integration_demos()
