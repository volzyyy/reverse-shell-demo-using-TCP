# reverse-shell-demo-using-TCP
# reverse-shell-demo-using-TCP

**Educational TCP Reverse-Shell Demo (Safe Version)**

---

## Overview
This project is an **educational demonstration** of a reverse-shell style client/server architecture using Python TCP sockets. It is designed to illustrate:

- TCP networking basics
- Message framing and delimiters
- Threaded input/output for interactive communication
- Safe remote command handling using a whitelist approach

> ⚠️ **Important:** This project is meant for learning purposes only. Run only on machines you own or in isolated lab environments (VMs, containers). Never attempt to access machines you do not own.

---

## Features

- **Client**
  - Connects back to a server (reverse connection)
  - Reports basic system information (IP, machine type, OS)
  - Executes only a small whitelist of pre-defined commands (e.g., `IPCONFIG`, `PING`)
  - Sends output back to the server

- **Server**
  - Listens for incoming client connections
  - Sends commands to connected clients
  - Receives and prints client responses
  - Supports interactive communication without blocking using threads

---

## Getting Started

### Requirements
- Python 3.x
- Optional: `requests` library (if you want the client to fetch external IP info)

```bash
pip install requests
