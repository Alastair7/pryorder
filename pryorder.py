import time
from pathlib import Path

def is_old_folder(folder):    
    delta = time.time() - folder.stat().st_mtime
    delta = delta / (60*60*24)

    if delta > 60:
        return True
    
    return False

# Get current path
current_path = Path(".")

# Check for unused folders
directories = [item for item in current_path.iterdir() if item.is_dir() if is_old_folder(item)]

# List unused folders
print(f"Found {len(directories)} unused directories")
print("Consider deleting this directories >> ", directories)