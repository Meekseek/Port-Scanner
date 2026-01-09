# Python Port Scanner

A lightweight network reconnaissance tool built in Python. This script utilizes the `socket` library to perform TCP connect scans, identifying open ports and active services on a target machine.

### 🚀 Features
* **TCP Connect Scan:** reliable detection of open ports.
* **Socket Handling:** demonstrates low-level networking in Python.
* **Error Management:** includes `try/except` blocks to handle keyboard interrupts and connection errors gracefully.

### 🛠️ Usage
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Meekseek/Port-Scanner.git](https://github.com/Meekseek/Port-Scanner.git)
    ```
2.  Run the scanner:
    ```bash
    python scanner.py
    ```
*(Note: By default, the script targets `10.0.0.1` for testing against home routers. You can modify the `target` variable in the source code to scan other IPs.)*

### ⚠️ Ethical Disclaimer
This tool is for **educational purposes and authorized testing only**. Scanning networks without permission is illegal. I built this to understand the underlying mechanics of TCP handshakes and network discovery.
