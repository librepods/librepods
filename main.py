
import platform

def check_os_type():
    """Check which type of OS is running"""
    os_type = platform.system()
    print(f"Detected OS: {os_type}")
    return os_type


def main():
    """Entry point for LibrePods."""
    check_os_type()


if __name__ == "__main__":
    main()
