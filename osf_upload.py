import subprocess
import os
from pathlib import Path

project_id = os.getenv("OSF_PROJECT_ID")
token = os.getenv("OSF_TOKEN")

def upload_folder(local_folder, remote_folder):
    path = Path(local_folder)
    if not path.exists():
        print(f"Skipping missing folder: {local_folder}")
        return

    for file in path.glob("*"):
        if not file.is_file():
            continue  # skip folders or junk

        print(f"Uploading {file} to OSF...")
        try:
            subprocess.run([
                "python", "-m", "osfclient",
                "-p", project_id,
                "--token", token,
                "upload",
                str(file),
                f"/{remote_folder}/{file.name}"
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to upload {file.name}: {e}")

upload_folder("notebooks", "notebooks")
upload_folder("converted", "converted")
