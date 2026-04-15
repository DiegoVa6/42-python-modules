print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
try:
    with open("lost_archive.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")

print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
try:
    with open("classified_vault.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")

print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
try:
    with open("standard_archive.txt", "r") as f:
        print("SUCCESS: Archive recovered "
              "- ``Knowledge preserved for humanity''")
        print("STATUS: Normal operations resumed\n")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained")
except Exception:
    print("RESPONSE: Unexpected system anomaly detected")
    print("STATUS: Crisis handled, system stabilized")


print("All crisis scenarios handled successfully. Archives secure.")
