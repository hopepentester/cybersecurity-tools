print("""
=============================
🔐  PYTHON PORT SCANNER v1.0
=============================
""")
import socket
import threading

# Function that scans a single port
def scan_port(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Set timeout for faster scanning
        result = sock.connect_ex((target, port))  # Try connecting

        if result == 0:
            print(f"✅ Port {port} is OPEN")

        sock.close()
    except socket.error as e:
        print(f"⚠️ Error scanning port {port}: {e}")

try:
    # Get user input
    target = input("Enter the IP address to scan: ")
    socket.inet_aton(target)  # Validate IP address format

    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    # Validate port range
    if start_port < 0 or end_port > 65535 or start_port > end_port:
        print("⚠️ Invalid port range. Ports must be between 0 and 65535.")
        exit()

    print(f"\n🔍 Scanning {target} from port {start_port} to {end_port}...\n")

    threads = []

    # Create a thread for each port and start scanning
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("\n✅ Scan complete.")

# Error handling
except ValueError:
    print("❌ Please enter valid numbers for ports.")
except socket.error:
    print("❌ Invalid IP address format.")
except KeyboardInterrupt:
    print("\n⛔ Scan interrupted by user.")
