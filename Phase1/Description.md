# 🛠️ Phase 1: Attack Setup and Execution

## 🔧 Environment Setup
- **Victim Machine:** Metasploitable3 (Ubuntu 14.04)
- **Attacker Machine:** Kali Linux (latest version)
- **Network:** Bridged adapter network between both VMs

## 🎯 Objective
To perform a brute-force SSH attack using:
1. Metasploit Framework (`ssh_login` module)
2. A custom Python script built with `paramiko`

## 📂 Tools & Files Used
- **Metasploit module:** `auxiliary/scanner/ssh/ssh_login`
- **Script:** `ssh_poc.py`
- **Wordlists:**  
  - `user.txt` – common usernames  
  - `password.txt` – weak/common passwords  
- Folder: `wordlists/`

## ✅ Execution Summary
- Both the Metasploit module and the custom script attempted SSH logins to the victim.
- Credentials `vagrant:vagrant` were discovered, allowing full access.
- Output from both methods was saved and captured as screenshots.

## ⚠️ Challenges Faced
- Initial SSH connection errors
- IP reachability between VMs
- Metasploit timing out on large wordlists

**Solutions:**
- Verified SSH port was open
- Added delays in Python script using `time.sleep()`
- Switched network adapter to ensure VM communication

## 🖼️ Screenshots Include:
- `metasploit-attack.png` – Metasploit attack in action
- `script-result.png` – Custom script showing login success
  
---

> **Note:** This attack was executed in a controlled lab environment for educational purposes only.
