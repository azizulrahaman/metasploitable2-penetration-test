import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

target = input("Enter target IP: ")
scan_ports(target, range(1, 1025))
