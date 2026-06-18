# Python Port Scanner

A TCP port scanner built in Python using the `socket` library.  
Available in two versions — single-threaded and multithreaded.  
Both versions print open ports in order, line by line.

---

## Versions

| File | Speed | How it works |
|---|---|---|
| `port_scanner.py` | Slower | Scans one port at a time, prints dots for closed ports |
| `port_scanner_fast.py` | Fast | Scans all ports simultaneously using threads |

---

## How to run

```bash
python3 port_scanner.py
```
```bash
python3 port_scanner_fast.py
```

You will be prompted to enter the target IP at runtime:

```
Enter the IP: 192.168.1.1
```

To change the port range or timeout, edit the config at the top of either file:

```python
start_port = 1
end_port   = 1024
timeout    = 0.5
```

---

## Example output

```
==================================================
Port Scanner
==================================================
Target IP  : 192.168.1.1
Port Range : 1 - 1024
Started at : 2024-06-18 10:30:00
--------------------------------------------------
.......................................
 [OPEN] port 22 ( ssh )
 [OPEN] port 80 ( http )
 [OPEN] port 443 ( https )
==================================================
Scan Complete. 3 open port(s) found.
==================================================
```

---

## Concepts covered

| Concept | Where it appears |
|---|---|
| TCP connection | `socket.connect_ex()` — tries to establish a connection |
| Port states | Return value `0` means open, anything else means closed |
| Timeouts | `settimeout()` prevents hanging on unresponsive ports |
| Service mapping | `getservbyport()` looks up IANA service names |
| Sorted output | `open_ports.sort()` prints results line by line in order |
| Multithreading | `threading.Thread` launches all 1024 scans simultaneously |
| Thread safety | `threading.Lock()` prevents race conditions on the shared list |
| Thread sync | `t.join()` waits for all threads to finish before printing |

---

## Legal & Ethical Notice

> Only scan IP addresses you own or have explicit permission to scan.  
> Scanning systems without permission is illegal under the Computer Fraud and Abuse Act (CFAA) and equivalent laws worldwide.  
> This tool is for **educational purposes only**.

---

## Built with

- Python 3
- `socket` (built-in)
- `datetime` (built-in)
- `threading` (built-in — fast version only)
