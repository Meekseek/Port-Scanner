import socket
import sys
from datetime import datetime

# Define the target: Your Router (10.0.0.1)
target = "10.0.0.1"

# Add a nice banner
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    # Scan ports 1 to 1024 (The "Well-Known" ports)
    for port in range(1, 1025):
        
        # Create a socket object (This is like picking up the phone)
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so we don't wait forever if a port is closed
        socket.setdefaulttimeout(0.05)
        
        # Try to connect. Returns 0 if successful
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        
        # Close the connection
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()

print("-" * 50)
print("Scan complete.")

