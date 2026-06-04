import os
import time

# 1. KINI ANG DICTIONARY (Ang 'Key' mao ang ngalan, ang 'Value' mao ang IP)
network_assets = {
    "Primary Gateway": "8.8.8.8",
    "Backup Server"  : "1.1.1.1"
}

print("=== CORE ASSET NETWORK SCANNER ===")
print("Operator: Master Kris | Device: Vivo V60\n")
time.sleep(1)

# 2. PAGKUHA OG DATA GAMIT ANG 'KEY'
print("[!] Ginasusi ang mga detalye sa unahan...")
time.sleep(0.5)

# Atong kuhaon ang saktong IP gamit ang ngalan sa Key
gateway_ip = network_assets["Primary Gateway"]
backup_ip = network_assets["Backup Server"]

print("-> Nakit-an ang Primary Gateway IP: " + gateway_ip)
print("-> Nakit-an ang Backup Server IP  : " + backup_ip)
print("----------------------------------------")
time.sleep(1)

# 3. PAGPATUYOK SA DICTIONARY (Gamit ang .items() aron dungan makuha ang Key ug Value)
print("[!] Nagsugod na ang Automated Asset Auditing:\n")

for ngalan, ip_address in network_assets.items():
    print("Testing Asset: " + ngalan + " [" + ip_address + "]")
    
    # I-ping ang IP address kausa (c 1)
    resulta = os.system("ping -c 1 " + ip_address)
    
    if resulta == 0:
        print("[✔️ ONLINE]: " + ngalan + " is fully operational.\n")
    else:
        print("[❌ OFFLINE]: " + ngalan + " cannot be reached.\n")
        
    time.sleep(1)

print("========================================")
print("[+] CORE AUDIT COMPLETE: Selyado ang duha ka assets.")
