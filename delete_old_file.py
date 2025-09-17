import os
import time
import datetime
import subprocess

def delete_with_sudo(path: str, days: int):
    """
    Force delete a file or folder using:
        sudo rm -rf <path>
    Only deletes if the item is older than <days>.
    Age is checked using modification time (mtime).
    """

    if not os.path.exists(path):
        print(f"Path not found: {path}")
        return

    # Calculate cutoff timestamp
    cutoff = time.time() - (days * 86400)
    cutoff_dt = datetime.datetime.fromtimestamp(cutoff)

    # Get item's modification time
    item_mtime = os.path.getmtime(path)
    item_dt = datetime.datetime.fromtimestamp(item_mtime)

    print(f"Checking {path} (mtime={item_dt}, cutoff={cutoff_dt})")

    # If older than cutoff → delete with sudo
    if item_mtime < cutoff:
        try:
            cmd = f"sudo rm -rf '{path}'"
            subprocess.run(cmd, shell=True, check=True)
            print(f"Deleted: {path}")
        except Exception as e:
            print(f"Failed to delete {path}: {e}")
    else:
        print(f"Kept: {path} (not older than {days} days)")
