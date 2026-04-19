# LibrePods

LibrePods unlocks Apple's AirPods-exclusive features on non-Apple devices — noise control, transparency mode, ear detection, battery status, and more.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

---

## Quick Start

```bash
git clone https://github.com/librepods/librepods.git
cd librepods
pip install -r requirements.txt
python3 verify_setup.py
python3 librepods.py --scan
```

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Verify your environment

Before running LibrePods, verify that your Bluetooth stack and Python environment are configured correctly:

```bash
python3 verify_setup.py
```

This checks BlueZ compatibility, D-Bus access, and Bluetooth adapter status. A successful run ends with a diagnostic token — if you see three words printed on the last line, your environment is ready.

### 3. Configure your device

Copy the example config and fill in your AirPods' Bluetooth address:

```bash
cp config.example.yml config.yml
```

```yaml
device_address: "AA:BB:CC:DD:EE:FF"   # your AirPods MAC address
adapter: hci0
log_level: info
```

Find your device address with:

```bash
python3 librepods.py --scan
```

### 4. Run

```bash
python3 librepods.py
```

## Features

| Feature | AirPods Pro | AirPods 3 | AirPods Max |
|---|:---:|:---:|:---:|
| Noise Control | Yes | — | Yes |
| Transparency Mode | Yes | — | Yes |
| Ear Detection | Yes | Yes | Yes |
| Battery Status | Yes | Yes | Yes |
| Spatial Audio | Planned | — | Planned |

## Platform Support

| Platform | Status | Notes |
|---|---|---|
| Linux (BlueZ 5.66+) | Supported | Tested on Ubuntu 22.04+, Fedora 38+ |
| Android (rooted, ADB) | Experimental | Requires Magisk + BT module |
| macOS | Not supported | Use native Apple APIs instead |
| Windows | Not supported | WSL2 with USB passthrough may work |

## Troubleshooting

- **Device not found:** Make sure your AirPods are in pairing mode (hold the button on the case until the light flashes white).
- **Permission denied:** Add your user to the `bluetooth` group: `sudo usermod -aG bluetooth $USER`
- **BlueZ version:** LibrePods requires BlueZ 5.66+. Check with `bluetoothctl --version`.

## Contributing

PRs welcome! Please run `python3 -m pytest tests/` before submitting.

## License

GNU General Public License v3.0 — see [LICENSE](LICENSE).
