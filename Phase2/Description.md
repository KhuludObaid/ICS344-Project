# 📊 Phase 2: SIEM Log Analysis using Splunk

## 🔧 Setup Summary
- **SIEM Tool Used:** Splunk Enterprise
- **Data Source:** `/var/log/auth.log` from the victim machine (Metasploitable3)
- **Log Forwarding:** Configured using Splunk Universal Forwarder
- **Environment:** Splunk installed on Kali Linux

## 🎯 Objective
To analyze SSH brute-force attack logs from Phase 1 using a Security Information and Event Management (SIEM) platform. Our goal was to visualize patterns in authentication failures and correlate them with attack activity.

## 📈 Dashboard Panels Created
- **Failed SSH Attempts Over Time**
- **Successful SSH Attempts Over Time** 
- **Most Attacked Usernames**  
- **Login Attempts by Hour**  
- **Login Outcome Breakdown (Success vs Fail)**  
- **Raw Log View of "Failed password" and "Accepted password" entries**

Each panel helped us identify the attack timeline, targeted usernames, and the success rate of brute-force attempts.

## 🔍 Observations
- **High-frequency login failures** from a single attacker IP.
- Common usernames such as `root`, `admin`, and `vagrant` were targeted repeatedly.

## 📊 Victim vs Attacker Log Comparison
- Victim logs in Splunk showed exact timestamps and usernames matching the output of our Metasploit and custom script attacks from Kali.
- This confirmed accurate log ingestion and alignment between attacker actions and victim-side logs.

## 🖼️ Screenshots Include:
- `dashboard-overview.png` – Full dashboard layout
- `log-analysis.png` – Timeline comparison of events

---

> **Note:** The SIEM platform helped us confirm the attack patterns and paved the way for the defense strategy in Phase 3.
