import socket

def scan_ports(target, ports=range(1, 1025)):
    print(f"\n[*] Scanning ports on {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except socket.error:
            print(f"[-] Could not connect to port {port}")
