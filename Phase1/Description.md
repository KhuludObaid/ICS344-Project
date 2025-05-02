# 🛠️ Phase 1: Attack Setup and Execution

---

## 🔧 Environment Setup

- **Victim Machine:** Metasploitable3 (Ubuntu 14.04)
- **Attacker Machine:** Kali Linux (latest)
- **Network Configuration:** Bridged Adapter for LAN communication

### 📍 Victim IP Address
<p align="center">
  <img src="Screenshots/Environment/victim-ip-address.jpg" width="500"/>
</p>

### 🔍 Nmap Scan Results
```bash
nmap -sV 192.168.8.116
```

<p align="center">
  <img src="Screenshots/Environment/nmap-scan.jpg" width="600"/>
  <br><em>Figure: Port 22 (SSH) is open on the victim</em>
</p>

---

## 🎯 Objective

To successfully brute-force SSH access on the victim machine using:
1. Metasploit (`ssh_login` module)
2. Custom Python script with `paramiko`

---

## 🧰 Tools Used

| Tool          | Description                              |
|---------------|------------------------------------------|
| Metasploit    | SSH login scanner module (`ssh_login`)   |
| `ssh_poc.py`  | Python script using `paramiko`            |
| `user.txt`    | Common usernames                         |
| `password.txt`| Weak passwords                           |

---

## 💥 Attack Execution

### 🔹 Metasploit Brute-force

```bash
use auxiliary/scanner/ssh/ssh_login
set RHOSTS 192.168.8.116
set USER_FILE /home/kali/user.txt
set PASS_FILE /home/kali/password.txt
run
```

<p align="center">
  <img src="Screenshots/Metasploit/metasploit-launch.jpg" width="500"/>
  <br><em>Launching Metasploit</em>
</p>

<p align="center">
  <img src="Screenshots/Metasploit/metasploit-config.jpg" width="500"/>
  <br><em>Configured module with wordlists</em>
</p>

<p align="center">
  <img src="Screenshots/Metasploit/metasploit-attack.jpg" width="500"/>
  <br><em>Login successful: Found credentials</em>
</p>

---

### 🔹 Python Script Brute-force

<p align="center">
  <img src="Screenshots/Script/script-userlist.jpg" width="400"/>
  <br><em>Username list</em>
</p>

<p align="center">
  <img src="Screenshots/Script/script-passwordlist.jpg" width="400"/>
  <br><em>Password list</em>
</p>

<p align="center">
  <img src="Screenshots/Script/script-code.jpg" width="500"/>
  <br><em>Key snippet of `ssh_poc.py`</em>
</p>

<p align="center">
  <img src="Screenshots/Script/script-result.jpg" width="500"/>
  <br><em>Script output: Found valid login</em>
</p>

---

## ✅ Outcome

- **Credentials found:** `vagrant : vagrant`
- **Access achieved** using both Metasploit and script
- Screenshots confirm end-to-end success

---

## ⚠️ Challenges & Solutions

| Challenge | Solution |
|----------|----------|
| SSH timeout | Used `time.sleep(0.8)` between attempts |
| Network issues | Switched to Bridged Adapter |
| Metasploit stalls | Limited wordlist size |

---

## 🔒 Disclaimer

> This lab was conducted in a controlled environment and is strictly for educational purposes.  
> Unauthorized access to any system is illegal and unethical.

---

✅ *Phase 1 completed – moving to log collection in Phase 2.*


