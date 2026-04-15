print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

filename = "new_discovery.txt"
file = None

print("Initializing new storage unit: new_discovery.txt")
file = open(filename, "w")
print("Storage unit created successfully...\n")

print("Inscribing preservation data...")

file.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
file.write("{[}ENTRY 002{]} Efficiency increased by 347 %\n")
file.write("{[}ENTRY 003{]} Archived by Data Archivist trainee\n")

if file is not None:
    file.close()

file = open(filename, "r")
print(file.read())

if file is not None:
    file.close()
print("Data inscription complete. Storage unit sealed.")
print("Archive 'new_discovery.txt' ready for long-term preservation.")
