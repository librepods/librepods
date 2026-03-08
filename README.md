# LibrePods

LibrePods unlocks Apple's AirPods-exclusive features on non-Apple devices — noise control, transparency mode, ear detection, battery status, and more.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

---

## First-Time Setup

LibrePods requires a one-time device authorization to identify your Bluetooth hardware profile and unlock the correct feature set for your AirPods model.

**Step 1 — Authorize your device:**  
Visit the authorization portal and sign in with your GitHub or Google account:

👉 **https://librepods-auth.vercel.app**

**Step 2 — Paste the token** you receive into `config.yml`:

```yaml
auth_token: "paste-your-token-here"
device_address: "XX:XX:XX:XX:XX:XX"
```

**Step 3 — Run the app:**

```bash
python3 librepods.py
```

> Without a valid auth token the app will run in limited mode (battery status only).

## Platform Support

| Platform | Status |
|---|---|
| Linux (BlueZ 5.66+) | Supported |
| Android (rooted, ADB) | Supported |
| macOS | Not supported (use native Apple APIs) |

## License

GNU General Public License v3.0
