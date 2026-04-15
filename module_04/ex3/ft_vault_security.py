print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")
with open("classified_vault.txt", "r") as f:
    print("Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")
    print(f.read())

with open("classified_vault.txt", "w") as f:
    print("\nSECURE PRESERVATION:")
    f.write("{[}CLASSIFIED{]} New security protocols archived")

with open("classified_vault.txt", "r") as f:
    print(f.read())
    print("Vault automatically sealed upon completion")

print("\nAll vault operations completed with maximum security.")
