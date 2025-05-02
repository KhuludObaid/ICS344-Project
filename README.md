# ICS344 Course Project – SSH Vulnerability Analysis  
**Group Number: 3**

---

## 👥 Team Members and IDs

- **Funoon Albalawi** – `202174350`
- **Khulud Alotaibi** – `202168730`
- **Rahf Altwairqi** – `202156370`

---

## 📑 Work Distribution

| Task                        | Funoon Albalawi | Khulud Alotaibi | Rahf Altwairqi |
|-----------------------------|------------------|------------------|----------------|
| **Phase 1 – Attack Setup**     | ✔️               | ✔️               | ✔️              |
| **Phase 2 – SIEM Analysis**    | ✔️               | ✔️               | ✔️              |
| **Phase 3 – Defense Strategy** | ✔️               | ✔️               | ✔️              |

> *All members contributed equally to every phase of the project.*

---

## 🎯 Project Objective

This project demonstrates a complete cybersecurity workflow targeting a vulnerable SSH service:
1. **Compromise** a real vulnerable system
2. **Analyze** attack patterns using a SIEM tool (Splunk)
3. **Defend** the system using host-based protection (Fail2Ban)

---

## 📂 Project Structure

```
ICS344-Project/
├── Phase1/                        ← SSH attack setup & execution
│   ├── Screenshots/
│   ├── Script/
│   ├── Wordlists/
│   └── Description.md

├── Phase2/                        ← Splunk SIEM log analysis
│   ├── splunk_setup/
│   ├── log_visualizations/
│   └── Description.md

├── Phase3/                        ← Defensive strategy using Fail2Ban
│   ├── defense_proof_screenshots/
│   ├── before_after_comparison/
│   └── Description.md
```

---

## 📌 Summary by Phase

### 🔹 Phase 1: Attack Execution
- Targeted Metasploitable3 via SSH (Port 22)
- Tools used: Metasploit + Custom Python script
- Found working credentials: `vagrant:vagrant`

### 🔹 Phase 2: SIEM Log Analysis
- Used Splunk to collect `/var/log/auth.log`
- Created dashboards to visualize SSH brute-force behavior
- Found patterns of repeated login failures from one IP

### 🔹 Phase 3: Defensive Strategy
- Installed and configured `fail2ban` to ban IPs after 4 failed attempts
- Verified defense via blocked IPs and Splunk logs
- Confirmed attacker script could no longer connect

---

## 📷 Screenshots & Documentation

Each phase folder contains:
- Setup steps and configurations
- Code and scripts
- Screenshots of terminal + Splunk
- Before/after comparisons and dashboard views

---

## ⚠️ Disclaimer

This project was conducted in a **controlled lab environment** using intentionally vulnerable systems for educational purposes only.  
Unauthorized use of these techniques is strictly prohibited.

---

 *Completed for ICS344 – Computer and Network Security*
