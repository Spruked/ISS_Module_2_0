from forensic_time_plugin import ForensicTimePlugin, ForensicConfig

# Initialize
plugin = ForensicTimePlugin(ForensicConfig(
    node_id="ISS_MODULE",
    storage_path="./forensic_logs"
))

# Generate pulse
pulse = plugin.pulse()

# Verify chain integrity
report = plugin.verify()  # Returns CLEAN or VIOLATED