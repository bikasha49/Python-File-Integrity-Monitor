import os
import hashlib
import time

TARGET_DIR = "./Target"
BASELINE_FILE = "baseline.txt"

def calculate_file_hash(filepath):
    """Calculates the SHA-512 hash of a file."""
    sha512_hash = hashlib.sha512()
    try:
        with open(filepath,"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha512_hash.update(byte_block)
        return sha512_hash.hexdigest()
    except FileNotFoundError:
        return None

def load_baseline():
    """Loads the baseline.txt into a dictionary."""
    baseline = {}
    if os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "r") as f:
            for line in f:
                path, h = line.strip().split("|")
                baseline[path] = h
    return baseline

print("\n--- File Integrity Monitor (Kali Edition) ---")
print("What would you like to do?")
print("    A) Collect new Baseline?")
print("    B) Begin Monitoring files with saved Baseline?")
response = input("\nPlease enter 'A' or 'B': ").upper()

if response == "A":
    if os.path.exists(BASELINE_FILE):
        os.remove(BASELINE_FILE)

    files = [f for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f))]

    with open(BASELINE_FILE, "w") as f:
        for file in files:
            path = os.path.join(TARGET_DIR, file)
            file_hash = calculate_file_hash(path)
            f.write(f"{path}|{file_hash}\n")

    print(f"\n[+] Baseline Collected! Saved to {BASELINE_FILE}")

elif response == "B":
    if not os.path.exists(BASELINE_FILE):
        print("\n[!] No baseline found. Please run Option A first.")
        exit()

    print("\n[*] Monitoring Started... (Press Ctrl+C to stop)")

    file_hashes = load_baseline()

    try:
        while True:
            time.sleep(1)

            current_files = [f for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f))]

            for file in current_files:
                path = os.path.join(TARGET_DIR, file)
                current_hash = calculate_file_hash(path)

                if path not in file_hashes:
                    print(f"[NEW] File created: {path}")
                    file_hashes[path] = current_hash

                elif file_hashes[path] != current_hash:
                    print(f"[CHANGED] File modified: {path}")
                    file_hashes[path] = current_hash 

            for path in list(file_hashes.keys()):
                if not os.path.exists(path):
                    print(f"[DELETED] File removed: {path}")
                    del file_hashes[path]

    except KeyboardInterrupt:
        print("\n[!] Monitoring Stopped.")