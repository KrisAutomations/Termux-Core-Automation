import os
import time

# 1. KINI ANG LIST (ARRAY) - Nagpundo og upat ka managlahing servers
mga_server = ["google.com", "facebook.com", "youtube.com", "github.com"]

print("=== AUTOMATED MULTI-SERVER AUDITOR ===")
print("Operator: Master Kris | Hardware: Vivo V60")
print("Nagsugod na ang pag-audit sa tanang servers sa listahan...\n")
time.sleep(1)

# 2. ANG GAHUM SA 'FOR LOOP' (Gisulod gamit ang saktong 'in' keyword)
for target in mga_server:
    print("----------------------------------------")
    print("[!] Ginasusi ang koneksyon ngadto sa: " + target)
    time.sleep(0.5)
    
    # Padaganon ang ping command kausa (c 1) para paspas ang audit
    resulta = os.system("ping -c 1 " + target)
    
    if resulta == 0:
        print("[✔️ STATUS]: " + target + " kay ONLINE ug ACTIVE.")
    else:
        print("[❌ ALERT ]: " + target + " kay OFFLINE o REBELDE.")
        
    time.sleep(1) # Preno kadiyot aron makita ang dagan sa matag server

print("========================================")
print("[+] AUDIT COMPLETE: Nadagan na ang tanang servers.")
