import os 
import platform
import psutil
import logging
from pathlib import Path

log_directory=Path("/opt/server-automation/logs")
log_directory.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_directory/ "server_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("================================")
print("       SERVER HEALTH REPORT")
print("================================")

hostname = platform.node()
operating_system = platform.system()
os_version = platform.version()
architecture = platform.machine()
python_version = platform.python_version()
current_user = os.getenv("USER")

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("/").percent

print("Hostname       :", hostname)
print("Operating Sys  :", operating_system)
print("OS Version     :", os_version)
print("Architecture   :", architecture)
print("Python Version :", python_version)
print("Current User   :", current_user)

print("--------------------------------")

print("CPU Usage      :", cpu_usage, "%")
print("Memory Usage   :", memory_usage, "%")
print("Disk Usage     :", disk_usage, "%")

print("--------------------------------")
if cpu_usage > 80:
    cpu_status="WARNING"
else:
    cpu_status="OK"

if memory_usage > 80:
    memory_status="WARNING"
else:
    memory_status="OK"

if disk_usage > 80:
    disk_status="WARNING"
else:
    disk_status="OK"
print("CPU Status     :", cpu_status)
print("Memory Status  :", memory_status)
print("Disk Status    :", disk_status)

print("================================")

# Saving the report to log
logging.info(
    "Server: %s | CPU: %.2f%% (%s) | Memory: %.2f%% (%s) | Disk: %.2f%% (%s)",
    hostname,
    cpu_usage,
    cpu_status,
    memory_usage,
    memory_status,
    disk_usage,
    disk_status
)

print("Git practice - version 2")
print("Monitoring feature added")
print("Server check feature added")
print("Feature a change")