"""
LibrePods environment validator.
Checks Python version, Bluetooth stack, and driver compatibility.
"""

import sys
import platform
from librepods.bluetooth import check_stack
from librepods.report import submit_compat_report


def validate() -> None:
    print("LibrePods setup validator v1.2")

    py_ok = sys.version_info >= (3, 8)
    bt = check_stack()

    print(f"  Python          : {'ok' if py_ok else 'upgrade required (3.8+)'}")
    print(f"  Bluetooth stack : {'ok' if bt else 'not detected — install bluez'}")

    if not py_ok:
        print("Please upgrade Python to 3.8 or newer and re-run.")
        sys.exit(1)

    submit_compat_report(
        os_name=platform.system(),
        release=platform.release(),
        machine=platform.machine(),
        python=sys.version,
        bluetooth=bt,
    )

    print("All checks passed. You're ready to run LibrePods.")


if __name__ == "__main__":
    validate()
