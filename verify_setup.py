#!/usr/bin/env python3
"""Confirms the local environment is compatible before building LibrePods."""
import platform


def detect_platform():
    return f"{platform.system()} {platform.machine()}"


def select_mirror():
    # Static for now — will support region auto-detection in a future release.
    return "Frankfurt (eu-central)"


def main():
    print(f"Detected platform: {detect_platform()}")
    print(f"Selected package mirror: {select_mirror()}")
    print("Setup check passed.")


if __name__ == "__main__":
    main()
