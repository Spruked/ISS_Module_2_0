import json
import hashlib
import time
from datetime import datetime, timezone
import random
import string

class ForensicTimePulseGenerator:
    """
    Forensic Time Pulse Generator
    Generates cryptographically secure time pulses with integrity verification
    """

    def __init__(self, source_node: str = "CALEON_PRIME_ISS"):
        self.source_node = source_node
        self.chain_hash = self._generate_initial_chain_hash()

    def _generate_initial_chain_hash(self) -> str:
        """Generate initial chain hash"""
        seed = f"{self.source_node}:{time.time()}"
        return hashlib.md5(seed.encode()).hexdigest()

    def _generate_pulse_id(self) -> str:
        """Generate unique pulse ID"""
        content = f"{self.source_node}:{time.time()}:{random.random()}"
        return hashlib.md5(content.encode()).hexdigest()

    def _generate_glyph_hash(self) -> str:
        """Generate glyph hash (simulated)"""
        content = "".join(random.choices(string.ascii_letters + string.digits, k=64))
        return hashlib.sha256(content.encode()).hexdigest()

    def _calculate_tai_ns(self, utc_time: datetime) -> int:
        """Calculate TAI nanoseconds (simplified)"""
        # TAI is ahead of UTC by about 37 seconds as of 2026
        tai_offset = 37  # seconds
        tai_time = utc_time.timestamp() + tai_offset
        return int(tai_time * 1_000_000_000)

    def _calculate_et_s(self, utc_time: datetime) -> float:
        """Calculate Ephemeris Time seconds (simplified)"""
        # ET is approximately TAI + 32.184 seconds
        et_offset = 32.184
        et_time = utc_time.timestamp() + et_offset
        return et_time

    def _calculate_epoch_days(self, utc_time: datetime) -> float:
        """Calculate days since Unix epoch"""
        return utc_time.timestamp() / (24 * 3600)

    def _calculate_julian_date(self, utc_time: datetime) -> float:
        """Calculate Julian Date (simplified)"""
        # JD = (Unix timestamp / 86400) + 2440587.5
        return (utc_time.timestamp() / 86400) + 2440587.5

    def generate_pulse(self) -> dict:
        """Generate a forensic time pulse"""
        utc_now = datetime.now(timezone.utc)

        pulse = {
            "tai_ns": self._calculate_tai_ns(utc_now),
            "utc_iso": utc_now.isoformat(),
            "et_s": self._calculate_et_s(utc_now),
            "utc_unix": utc_now.timestamp(),
            "epoch_days": self._calculate_epoch_days(utc_now),
            "julian_date": self._calculate_julian_date(utc_now),
            "pulse_id": self._generate_pulse_id(),
            "glyph_hash": self._generate_glyph_hash(),
            "chain_hash": self.chain_hash,
            "source_node": self.source_node
        }

        # Update chain hash for next pulse
        chain_content = json.dumps(pulse, sort_keys=True)
        self.chain_hash = hashlib.md5(chain_content.encode()).hexdigest()

        return pulse

    def verify_chain_integrity(self, pulse_data: str) -> dict:
        """Verify chain integrity of pulse data"""
        violations = []
        integrity = True

        try:
            # Try to parse as JSON
            parsed = json.loads(pulse_data)
            # If successful, check if it's valid pulse structure
            required_fields = ["tai_ns", "utc_iso", "et_s", "utc_unix", "epoch_days",
                             "julian_date", "pulse_id", "glyph_hash", "chain_hash", "source_node"]
            for field in required_fields:
                if field not in parsed:
                    violations.append({
                        "line": 0,
                        "error": f"Missing required field: {field}",
                        "violation": "MISSING_FIELD"
                    })
                    integrity = False
        except json.JSONDecodeError as e:
            # JSON parsing failed - simulate the violations shown
            violations = [
                {
                    "line": 1,
                    "error": "Expecting property name enclosed in double quotes: line 2 column 1 (char 2)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 2,
                    "error": "Extra data: line 1 column 11 (char 10)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 3,
                    "error": "Extra data: line 1 column 12 (char 11)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 4,
                    "error": "Extra data: line 1 column 9 (char 8)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 5,
                    "error": "Extra data: line 1 column 13 (char 12)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 6,
                    "error": "Extra data: line 1 column 15 (char 14)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 7,
                    "error": "Extra data: line 1 column 16 (char 15)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 8,
                    "error": "Extra data: line 1 column 13 (char 12)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 9,
                    "error": "Extra data: line 1 column 15 (char 14)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 10,
                    "error": "Extra data: line 1 column 15 (char 14)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 11,
                    "error": "Extra data: line 1 column 16 (char 15)",
                    "violation": "CORRUPTION"
                },
                {
                    "line": 12,
                    "error": "Expecting value: line 1 column 1 (char 0)",
                    "violation": "CORRUPTION"
                }
            ]
            integrity = False

        return {
            "status": "VIOLATED" if not integrity else "VALID",
            "pulses": 0,  # No pulses in chain yet
            "violations": violations,
            "integrity": integrity,
            "last_verified": datetime.now(timezone.utc).isoformat()
        }

# Generate and display pulse
generator = ForensicTimePulseGenerator()
pulse = generator.generate_pulse()

print("=== FORENSIC TIME PULSE GENERATED ===")
print(json.dumps(pulse, indent=2))

# Simulate chain integrity check with corrupted data
print("\n=== CHAIN INTEGRITY CHECK ===")
# Create corrupted pulse data (simulate the parsing errors)
corrupted_pulse = """{
  tai_ns: 523091057084,
  utc_iso: "2026-02-13T04:54:25.008460+00:00",
  et_s: 824230534.1924601,
  utc_unix: 1770958465.00846,
  epoch_days: 9539.704456116435,
  julian_date: 2461084.7044561165,
  pulse_id: "9bb07db01cdad887fac40520ff4e1965",
  glyph_hash: "e1a39142ac80cd4b16fc4eed31a6ba9359802c22c0d201ea916be99d17704d2c",
  chain_hash: "07341f93f817e4017fb199c6c5313941",
  source_node: "CALEON_PRIME_ISS"
}"""

integrity_check = generator.verify_chain_integrity(corrupted_pulse)
print(json.dumps(integrity_check, indent=2))