🛡️ PyGuardian-Scanner

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Security](https://img.shields.io/badge/focus-Cyber%20Security-red)

**PyGuardian-Scanner** is a high-performance, multi-threaded network reconnaissance tool developed in Python. It efficiently scans network ports, identifies open services through banner grabbing, and handles network exceptions gracefully.

---

🎯 Project Overview
The objective of this project is to provide a fast and reliable port scanner that demonstrates **advanced networking concepts** and **concurrency** in Python. It is designed for security enthusiasts and network administrators to audit their local environments.

✨ Key Features
* **Multi-threaded Engine:** Optimized to scan hundreds of ports simultaneously using the `threading` library.
* **Service Banner Grabbing:** Automatically attempts to identify service names (e.g., HTTP, SSH, SMB, RPC) for each open port.
* **Performance:** Significantly faster than traditional sequential scanners.
* **Error Resilient:** Advanced `try-except` blocks to handle timeouts and socket-level errors.
* **User-Friendly Output:** Clean, timestamped terminal logs.

---

🛠️ Technical Stack
| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.11+ |
| **Network Engine** | `socket` (TCP Handshake) |
| **Parallelism** | `threading` |
| **Utilities** | `datetime`, `re` |

---

🚀 Getting Started

1. Installation
Clone the repository to your local machine:
```bash
git clone [https://github.com/CryzZ1/PyGuardian-Scanner.git](https://github.com/CryzZ1/PyGuardian-Scanner.git)
cd PyGuardian-Scanner
