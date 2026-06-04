import os
import time
import shutil  # Kini nga tool ang mobasa sa tinuod nga storage partition

master_name = "Master Kris"
phone_model = "Vivo V60"

print("=== CORE SYSTEM SCANNERS ===")
print("Scanning real-time Device hardware details...")
time.sleep(1)

# 1. REAL-TIME STORAGE EXTRACTION
# Atong basahon ang tinuod nga internal storage sa phone (/storage/emulated)
total, used, free = shutil.disk_usage("/storage/emulated")

# Inig kuha sa data, dako kaayo ni (Bytes). Atong i-convert ngadto sa GB (Gigabytes)
tinuod_total = total / (1024**3)
tinuod_used = used / (1024**3)
tinuod_nabilin = free / (1024**3)

# Pag-kalkula sa porsyento base sa tinuod nga dagan sa memory
porsyento_nagamit = (tinuod_used / tinuod_total) * 100

# 2. PAGPAGAWAS SA REPORT
print("\n========================================")
print("          SYSTEM PROFILE REPORT         ")
print("========================================")
print("System Operator : " + master_name)
print("Device Hardware : " + phone_model)
print("Total Storage   : " + str(round(tinuod_total, 2)) + " GB")
print("Used Storage    : " + str(round(tinuod_used, 2)) + " GB")
print("Available Space : " + str(round(tinuod_nabilin, 2)) + " GB")
print("Storage Usage   : " + str(round(porsyento_nagamit, 2)) + "%")
print("----------------------------------------")

# 3. DYNAMIC CONDITIONAL ALERT
if tinuod_nabilin < 5.0:
    print("[⚠️ WARNING]: Critical Storage Level! Paghinlo na, Master!")
else:
    print("[✔️ STATUS]: Luwas pa ang imong storage partition. Kombati!")
print("========================================")
