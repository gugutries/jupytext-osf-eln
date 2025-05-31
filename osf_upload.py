import subprocess
import os
from pathlib import Path

project_id = os.getenv("OSF_PROJECT_ID")

def upload_folder(local_folder, remote_folder):
    path = Path(local_folder)
    if not path.exists():
        return
    for file in path.glob("*.*"):
        print(f"Uploading {file} to OSF...")
        subprocess.run([
            "osf", "-p", project_id,
            "upload", str(file),
            f"/{remote_folder}/{file.name}"
        ])

upload_folder("notebooks", "notebooks")
upload_folder("converted", "converted")
