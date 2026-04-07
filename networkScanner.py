import socket
import threading
from datetime import datetime

# Target configuration
# Using a common local IP for testing purposes
TARGET = "127.0.0.1"
PORT_RANGE = range(1, 1025) # Scanning first 1024 ports
THREADS = 100 # Number of threads for faster execution

print(f"[*] Scanning Target: {TARGET}")
print(f"[*] Time Started: {datetime.now()}")

def ScanPort(port):
    """
    Attempts to connect to a specific port to check if it's open.
    Uses socket library for network connection.
    """
    try:
        # Creating a socket object (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Setting a short timeout for efficiency
        s.settimeout(0.5)
        
        # Attempting the connection (returns 0 if successful)
        result = s.connect_ex((TARGET, port))
        if result == 0:
            # Banner grabbing: Identifying the service running on the port
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"
            
            print(f"[+] Port {port} is OPEN ({service})")
        s.close()
        
    except socket.error as err:
        # Handling unexpected network errors
        pass

def RunScanner():
    """
    Manages threads to ensure the scan is fast and concurrent.
    This demonstrates intermediate level multi-threading skills.
    """
    for port in PORT_RANGE:
        # Creating a thread for each port scan
        t = threading.Thread(target=ScanPort, args=(port,))
        t.start()

if __name__ == "__main__":
    # Entry point of the script
    RunScanner()
