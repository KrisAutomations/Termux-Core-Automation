import os
import time

SECRET_PASSWORD = "master_kris_2026"

def dagan_ping(target_host):
    print("\n[!] Nagsugod na ang pag-test sa koneksyon ngadto sa: " + target_host)
    resulta = os.system("ping -c 3 " + target_host)
    if resulta == 0:
        status_text = "SUCCESS: Konektado ka sa " + target_host
    else:
        status_text = "FAILED: Dili ma-reach ang " + target_host
    print("\n[+] RESULTA: " + status_text)
    with open("network_log.txt", "a") as log_file:
        log_file.write(time.strftime("%Y-%m-%d %H:%M:%S") + " - " + status_text + "\n")

# --- MAIN SECURITY GATE ---
print("=== KRIS SECURE CORE TERMINAL ===")
sulod_password = input("Palihog i-enter ang SECURITY PASSWORD: ")

if sulod_password == SECRET_PASSWORD:
    print("\n[+] ACCESS GRANTED.")
    time.sleep(1)
    
    # KINI ANG SULOD SA INFINITE MENU LOOP
    while True:
        print("\n========================================")
        print("          MAIN CONTROL MENU             ")
        print("========================================")
        print("[1] I-Ping ang Network (Google/Website)")
        print("[2] Basahon ang Network Log History")
        print("[3] Limpyohan ang Screen (Clear)")
        print("[4] Susiha ang Storage sa Phone (df -h)")
        print("[5] Mo-Exit sa Sistema (Shut Down)")
        print("----------------------------------------")
        
        pili = input("Pilia ang imong Command (1-5): ")
        
        if pili == "1":
            target = input("\nI-enter ang Website o IP: ")
            dagan_ping(target)
            input("\nPindota ang ENTER aron mobalik sa Menu...")
            
        elif pili == "2":
            print("\n=== KASAYSAYAN SA LOGS ===")
            if os.path.exists("network_log.txt"):
                os.system("cat network_log.txt")
            else:
                print("Walay nakit-an nga log file.")
            input("\nPindota ang ENTER aron mobalik sa Menu...")
            
        elif pili == "3":
            os.system("clear")
            
        elif pili == "4":
            print("\n=== STATUS SA STORAGE SA PHONE ===")
            # Gidagan sa Python ang Linux command aron sutaon ang /storage/emulated
            os.system("df -h | grep -E 'Size|emulated'")
            input("\nPindota ang ENTER aron mobalik sa Menu...")
            
        elif pili == "5":
            print("\nShutting down core interface... Goodbye, Master Kris!")
            break
            
        else:
            print("\n[X] Invalid Option! Palihog pagpili gikan sa 1 hangtod 5.")
            time.sleep(1)
else:
    print("\n[X] ACCESS DENIED!")
