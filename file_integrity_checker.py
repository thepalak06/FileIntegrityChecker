'''
Created on 13-Jul-2025

@author: beher
'''
import hashlib
import os

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print("File not found.")
        return None

def save_hash(file_path, hash_value):
    with open(file_path + ".hash", "w") as f:
        f.write(hash_value)

def load_hash(file_path):
    try:
        with open(file_path + ".hash", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def main():
    file_path = input("Enter the path of the file to check: ").strip()

    if not os.path.isfile(file_path):
        print("Invalid file path!")
        return

    current_hash = calculate_hash(file_path)
    saved_hash = load_hash(file_path)

    if saved_hash:
        print(f"Previous hash: {saved_hash}")
        print(f"Current  hash: {current_hash}")
        if current_hash == saved_hash:
            print("✅ File integrity verified. No changes detected.")
        else:
            print("⚠️ File has been modified!")
    else:
        print("No saved hash found. Saving current hash for future comparison.")
        save_hash(file_path, current_hash)
        print("Hash saved.")

if __name__ == "__main__":
    main()

