print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

filename = "ancient_fragment.txt"
print(f"Accessing Storage Vault: {filename}")

try:
    f = open(filename, "r")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
else:
    try:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        data = f.read()
        print(data)
    finally:
        f.close()

    print("Data recovery complete. Storage unit disconnected.")
