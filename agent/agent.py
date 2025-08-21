


# import psutil
# import platform
# import requests
# import socket

# BACKEND_URL = "http://127.0.0.1:8000/api"

# def get_system_info():
#     return {
#         "hostname": socket.gethostname(),
#         "os": platform.system(),
#         "os_version": platform.version(),
#         "cpu_count": psutil.cpu_count(logical=True),
#         "total_memory": round(psutil.virtual_memory().total / (1024**3), 2),
#         "available_memory": round(psutil.virtual_memory().available / (1024**3), 2),
#         "disk_usage": round(psutil.disk_usage('/').total / (1024**3), 2)
#     }

# def get_process_info():
#     processes = []
#     for p in psutil.process_iter(['pid','ppid','name','memory_info','cpu_percent']):
#         try:
#             processes.append({
#                 "name": p.info['name'],
#                 "memory_usage": round(p.info['memory_info'].rss / (1024*1024), 2),
#                 "cpu_usage": p.info['cpu_percent'],
#                 "ppid": p.info['ppid']
#             })
#         except (psutil.NoSuchProcess, psutil.AccessDenied):
#             continue
#     return processes

# def system_exists(hostname):
#     try:
#         response = requests.get(f"{BACKEND_URL}/systeminfo/")
#         if response.status_code == 200:
#             systems = response.json()
#             for sys in systems:
#                 if sys.get("hostname") == hostname:
#                     return True
#     except Exception as e:
#         print(f"❌ Error checking system: {e}")
#     return False

# def send_data():
#     system_info = get_system_info()
#     hostname = system_info["hostname"]

#     # Check if system already exists
#     if system_exists(hostname):
#         print("⚠️ System data already exists, skipping system info upload...")
#     else:
#         requests.post(f"{BACKEND_URL}/systeminfo/", json=system_info)
#         print("✅ New system info sent successfully!")

#     # Always send process data (it changes frequently)
#     process_info = get_process_info()
#     for proc in process_info:
#         requests.post(f"{BACKEND_URL}/processinfo/", json=proc)

#     print("✅ Process data sent successfully!")

# if __name__ == "__main__":
#     send_data()




import psutil
import platform
import requests
import socket

BACKEND_URL = "http://127.0.0.1:8000/api"

def get_system_info():
    """Collect basic system information."""
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "cpu_count": psutil.cpu_count(logical=True),
        "total_memory": round(psutil.virtual_memory().total / (1024**3), 2),
        "available_memory": round(psutil.virtual_memory().available / (1024**3), 2),
        "disk_usage": round(psutil.disk_usage('/').total / (1024**3), 2)
    }

def get_process_info():
    """Collect running process information."""
    processes = []
    for p in psutil.process_iter(['pid', 'ppid', 'name', 'memory_info', 'cpu_percent']):
        try:
            processes.append({
                "name": p.info['name'],
                "pid": p.info['pid'],
                "ppid": p.info['ppid'],
                "memory_usage": round(p.info['memory_info'].rss / (1024*1024), 2),
                "cpu_usage": p.info['cpu_percent']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def system_exists(hostname: str) -> bool:
    """Check if the system already exists in backend."""
    try:
        response = requests.get(f"{BACKEND_URL}/systeminfo/", timeout=5)
        if response.status_code == 200:
            systems = response.json()
            return any(sys.get("hostname") == hostname for sys in systems)
        else:
            print(f"❌ Failed to check system info, status {response.status_code}")
    except Exception as e:
        print(f"❌ Error checking system: {e}")
    return False

def send_data():
    """Send system and process info to backend with logging."""
    system_info = get_system_info()
    hostname = system_info["hostname"]

    # Upload system info (only once)
    if system_exists(hostname):
        print("⚠️ System data already exists, skipping system info upload...")
    else:
        try:
            r = requests.post(f"{BACKEND_URL}/systeminfo/", json=system_info, timeout=5)
            if r.status_code in (200, 201):
                print("✅ New system info sent successfully!")
            else:
                print(f"❌ Failed to upload system info, status {r.status_code}")
        except Exception as e:
            print(f"❌ Error uploading system info: {e}")

    # Always upload process info
    try:
        process_info = get_process_info()
        if not process_info:
            print("⚠️ No process info collected.")
        else:
            for proc in process_info:
                requests.post(f"{BACKEND_URL}/processinfo/", json=proc, timeout=5)
            print("✅ Process data sent successfully!")
    except Exception as e:
        print(f"❌ Error uploading process data: {e}")

if __name__ == "__main__":
    send_data()
    input("\nPress Enter to exit...")  
