import socket

VULN_PORTS = {
    21: "FTP - Check for anonymous login",
    22: "SSH - Check for weak credentials",
    23: "Telnet - Unencrypted protocol",
    445: "SMB - Check for EternalBlue",
    3306: "MySQL - Check for open access",
    8080: "HTTP Alt - Check for admin panels"
}

def scan(target):
    print(f"\n[*] Scanning {target} for vulnerabilities...\n")
    for port, warning in VULN_PORTS.items():
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[!] Port {port} OPEN — {warning}")
        sock.close()

target = input("Enter target IP: ")
scan(target)
