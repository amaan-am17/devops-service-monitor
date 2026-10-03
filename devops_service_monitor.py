import subprocess
import requests
print("=======================")
print("DEVOPS SERVICE MONITOR")
print("=======================")
try:
    result = subprocess.run(
        ["ping", "-n", "1", "localhost"],
        capture_output=True,
        text=True,
        check=True
    )
    system_status = "HEALTHY"
except subprocess.CalledProcessError:
    system_status = "UNHEALTHY"
except FileNotFoundError:
    system_status = "UNHEALTHY"
print("SYSTEM CHECK:", system_status)
try:
    response = requests.get("https://httpbin.org/get", timeout=5)
    response.raise_for_status()
    api_status = "HEALTHY"
except requests.RequestException:
    api_status = "UNHEALTHY"
print("API CHECK:", api_status)
if system_status == "HEALTHY" and api_status == "HEALTHY":
    overall_status = "HEALTHY"
else:
    overall_status = "UNHEALTHY"
print("OVERALL STATUS:", overall_status)    
