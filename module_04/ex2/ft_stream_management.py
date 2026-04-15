import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

archivist_id = input("Input Stream active. Enter archivist ID: ")
status = input("Input Stream active. Enter status report: ")

sys.stdout.write(f"\n{{[}}STANDARD{{]}} "
                 f"Archive status from {archivist_id}: {status}\n")
sys.stderr.write("{[}ALERT{]} System diagnostic: "
                 "Communication channels verified\n")
sys.stdout.write("{[}STANDARD{]} Data transmission complete")

print("\n\nThree-channel communication test successful.")
