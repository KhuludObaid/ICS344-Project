import paramiko

ip = "192.168.8.112"
username = "vagrant"
password = "vagrant"

try:
    print(f"[+] Connecting to {ip} with {username}:{password}")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)

    stdin, stdout, stderr = ssh.exec_command("whoami")
    print("[+] Command output:", stdout.read().decode().strip())
    ssh.close()

except Exception as e:
    print("[-] Connection failed:", e)
