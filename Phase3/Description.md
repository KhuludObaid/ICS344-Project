# 🛡️ Phase 3: Defense Strategy with Fail2Ban

## 🔧 Setup Summary
- **Defense Tool:** Fail2Ban
- **Monitored Log File:** `/var/log/auth.log`
- **Platform:** Metasploitable3 (Ubuntu 14.04)
- **Configuration File:** `/etc/fail2ban/jail.local`

## 🎯 Objective
To automatically detect and block SSH brute-force attacks by banning the attacker’s IP address after multiple failed login attempts, using a log-based intrusion prevention tool.

## ⚙️ Configuration
We configured Fail2Ban with the following rules under `[sshd]`:
- `enabled = true`
- `port = ssh`
- `filter = sshd`
- `logpath = /var/log/auth.log`
- `maxretry = 3` (ban after 3 failures)
- `findtime = 600` (within 10 minutes)
- `bantime = 1800` (ban lasts 30 minutes)

After applying the settings, we restarted the Fail2Ban service and verified the SSH jail was active.

## 🧪 Testing the Defense
We reran the brute-force attack script from Kali. After 3 failed login attempts, Fail2Ban:
- **Detected the pattern**
- **Banned the attacker IP**
- **Blocked all future SSH attempts from that IP**

The IP ban was confirmed using:
```bash
sudo fail2ban-client status sshd

## 📉 Result Validation
- **Before defense**: Splunk showed a large number of failed SSH login attempts.
- **After defense**: The failed attempts dropped significantly as the attacker's IP was blocked.

## 🖼️ Screenshots Included
- `fail2ban-installed.png` – Confirmation of successful Fail2Ban installation
- `jail-local-config.png` – Configuration file showing maxretry and bantime values
- `before-ban-status.png` – Fail2Ban status before any IP was banned
- `after-ban-status.png` – Attacker IP listed as banned
- `kali-blocked-connection.png` – SSH access blocked after IP ban
- `splunk-before-defense.png` – Spike in failed login events before Fail2Ban
- `splunk-after-defense.png` – Drop in failed login events after defense was applied

## ⚠️ Challenges Faced
- Fail2Ban was not available via `apt` due to deprecated Ubuntu 14.04 repositories
- Solved by manually downloading and installing the `.deb` package from a legacy source

---

> **Note:** This defense phase demonstrates the effectiveness of combining log-based detection with automated IP banning to mitigate brute-force attacks.
