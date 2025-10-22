# reverse-shell-demo-using-TCP
# ⚠️ IMPORTANT NOTICE

**THIS IS A TEST/DEMO NOT THE FULL CODE. (FULL COMING LATER)**  
**NEED SOME BACKROUND KNOWLEDGE**

**Educational TCP Reverse-Shell Demo (Safe Version)**

---

## Overview
This project is an **educational demonstration** of a reverse-shell style client/server architecture using Python TCP sockets.
⚠️ **Important:** This project is meant for learning purposes only. Run only on machines you own or in isolated lab environments (VMs, containers). Never attempt to access machines you do not own.

---

## Features

- **Client**
  - Connects back to a server (reverse connection)
  - Reports basic system information (IP, machine type, OS)
  - Sends output back to the server

- **Server**
  - Listens for incoming client connections
  - Sends commands to connected clients
  - Receives and prints client responses
  - Supports interactive communication without blocking using threads

---

