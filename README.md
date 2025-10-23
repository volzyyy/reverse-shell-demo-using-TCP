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

## How to Run (Educational Demo)

> ⚠️ **Important:** Run this only on machines you own or in a controlled lab environment.

1. **Set the IP Address**
   - Edit both `server.py` and `client.py`.
   - Change the IP address to the machine you want the client to connect to (usually your own PC for testing).

2. **Start the Server**
   - Open a command terminal on the machine running `server.py`.
   - Run:
     ```bash
     python server.py
     ```
   - You should see a message like:
     ```
     Server is running and waiting for a connection...
     ```

3. **Start the Client**
   - On the same machine or another machine (your choice for testing), open a command terminal.
   - Run:
     ```bash
     python client.py
     ```
   - The client will connect to the server and send basic system info.

4. **Interact with the Server**
   - On the server terminal, once the client connects, you should see:
     ```
     Run Commands:
     ```
   - You can now type **predefined, safe commands** (like `IPCONFIG` on Windows or `PING`) and see the output from the client.

5. **Notes**
   - Only commands defined in the client’s whitelist are allowed. Arbitrary shell commands are **not supported** for safety.
   - Close the server or client to terminate the connection.
