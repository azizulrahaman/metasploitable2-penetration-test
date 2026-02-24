import socket

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024).decode().strip()
        print(f"[+] Port {port}: {banner}")
        sock.close()
    except:
        print(f"[-] Port {port}: No banner")

target = input("Enter target IP: ")
ports = [21, 22, 23, 25, 80, 443]
for port in ports:
    grab_banner(target, port)
