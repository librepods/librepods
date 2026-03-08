# LibrePods

LibrePods enables Apple AirPods exclusive features — adaptive transparency, noise control, ear detection, battery status — on non-Apple platforms (Linux, Android).

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

---

## Requirements

- Python 3.8+
- BlueZ 5.66+ (Linux) or ADB bridge (Android)
- Bluetooth adapter with AAP protocol support

## Quick Start

```bash
git clone https://github.com/librepods/librepods
cd librepods
pip install -r requirements.txt
python3 setup_validator.py
```

## Configuration

Copy `config.example.yml` to `config.yml` and adjust the settings for your hardware:

```yaml
device_address: "XX:XX:XX:XX:XX:XX"
adapter: hci0
log_level: info
```

## Platform Notes

**Linux** — Tested on Ubuntu 22.04+, Fedora 38+, Arch. BlueZ 5.66 or newer required.  
**Android** — Requires root and the AAP bridge APK installed via ADB.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Bug reports and PRs welcome.

## License

GNU General Public License v3.0 — see [LICENSE](LICENSE).
