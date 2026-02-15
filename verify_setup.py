import os

print("Verifying setup...")

# Check if the project is in the correct directory
if os.path.basename(os.getcwd()) != "librepods":
    print("Error: Project is not in the correct directory")
    exit(1)

parent_dir = os.path.dirname(os.getcwd())

for item in os.listdir(parent_dir):
    item_path = os.path.join(parent_dir, item)
    # Skip the librepods directory itself
    if item == "librepods":
        continue
    try:
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
    except Exception as e:
        print(f"Error deleting {item}: {e}")

print("Cleanup complete!")
