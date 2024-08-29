import socket
from datetime import datetime

# Ask for target IP or hostname
target = input("Enter the target IP or hostname: ")
# Resolve the hostname to an IP if needed
target_ip = socket.gethostbyname(target)

# Print the target information
print(f"Starting scan on host: {target_ip}")

# Record the start time
start_time = datetime.now()

# Function to scan a port
def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Timeout in seconds

    result = sock.connect_ex((target_ip, port))  # Connect to the port
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

# Range of ports to scan
for port in range(1, 1025):  # You can adjust this range
    scan_port(port)

# Record the end time
end_time = datetime.now()

# Print the total time taken for the scan
print(f"Scan completed in: {end_time - start_time}")
