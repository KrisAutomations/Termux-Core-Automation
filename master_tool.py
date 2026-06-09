import os
import time
import shutil

# KINI NGA FUNCTION ADUNAAY DUHA KA PARAMETERS: operator ug system_type
def suta_sistema(operator, system_type):
    print("\n[!] Pag-analisar sa sistema gisugdan na ni " + operator + "...")
    time.sleep(1)
    
    if system_type == "storage":
        total, used, free = shutil.disk_usage("/storage/emulated")
        nabilin = free / (1024**3)
        print("-> Resulta: Magamit pa nga memory: " + str(round(nabilin, 2)) + " GB")
        
    elif system_type == "network":
        print("-> Resulta: Nagsusi sa network latency dapit sa Agusan del Sur...")
        os.system("ping -c 2 google.com")
        
    else:
        print("-> [X] ERROR: Wala masabtan ang system type.")

# === MAIN RUNNING CODE ===
# Karon, atong tawgon ang function ug magpasa kita og managlahing ARGUMENTS!

# Unang Pagsulay (Test 1): Pagkuha sa Storage
suta_sistema("Master Kris", "storage")

print("\n----------------------------------------")

# Ikaduhang Pagsulay (Test 2): Pag-test sa Network
suta_sistema("Master Kris", "network")
# Version: 1.0.1 - Hardware Profile: Vivo V60 optimized
