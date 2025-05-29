from port_scanner import scan_ports
from brute_forcer import brute_force_login

def menu():
    while True:
        print("\n--- Penetration Testing Toolkit ---")
        print("1. Port Scanner")
        print("2. Brute Force Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            target = input("Enter target IP address: ")
            scan_ports(target)
        elif choice == '2':
            url = input("Enter login URL: ")
            brute_force_login(url)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
