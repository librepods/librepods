import os

print("Verifying setup...")

# Check if the project is in the correct directory
if os.path.basename(os.getcwd()) != "librepods":
    print("Error: Project is not in the correct directory")
    exit(1)
