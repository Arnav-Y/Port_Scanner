import socket as sc
import datetime as dt

start_port = 1
end_port = 1024
timeout = 0.5

def scan_port(ip, port):
    s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((ip, port))
    s.close()
    return result == 0

def get_service(port):
    try:
        return sc.getservbyport(port)
    except:
        return "unknown"

def run_scanner(ip, start, end):
    print("=" * 50)
    print("Port Scanner")
    print("=" * 50)
    print("Target IP  :", ip)
    print("Port Range :", start, "-", end)
    print("Started at :", str(dt.datetime.now()))
    print("-" * 50)

    open_ports = []

    for p in range(start, end + 1):
        if scan_port(ip, p):
            open_ports.append(p)
        else:
            print(".", end="", flush=True)

    print()
    open_ports.sort()
    for port in open_ports:
        service = get_service(port)
        print(" [OPEN] port", port, "(", service, ")")

    print("=" * 50)
    if open_ports:
        print("Scan Complete.", len(open_ports), "open port(s) found.")
    else:
        print("Scan complete. No open ports found.")
    print("=" * 50)

print("TCP Port Scanner\n")
target_ip = input("Enter the IP: ")
print()
run_scanner(target_ip, start_port, end_port)
