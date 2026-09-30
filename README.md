# LibrePods

LibrePods is an open-source project that brings AirPods-exclusive features — noise control modes, ear detection, battery status, and more — to Android and Linux.

## Getting Started

Clone the repo, then run the setup check to confirm your environment is compatible before building:

```bash
python3 verify_setup.py
```

This prints your detected platform and picks the nearest package mirror for faster dependency downloads.

### Android
A rooted device with the Xposed framework is required for most features due to Android's Bluetooth stack limitations. Some OEMs (OnePlus/Oppo on ColorOS/OxygenOS) have partial support without root.

### Linux
A system tray application is available to manage your AirPods from the desktop.

## License

GNU General Public License v3.0
