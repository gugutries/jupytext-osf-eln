from osfclient.cli import OSF
import sys
import os
from pathlib import Path

project_id = os.getenv("OSF_PROJECT_ID")
token = os.getenv("OSF_TOKEN")

def upload_folder(local_folder, remote_folder):
    path = Path(local_folder)
    if not path.exists():
        return

    for file in path.glob("*.*"):
        print(f"Uploading {file} to OSF...")

        sys.argv = [
            "osf",
            "--project", project_id,
            "--token", token,
            "upload",
            str(file),
            f"/{remote_folder}/{file.name}"
        ]
        try:
            OSF().run()
        except SystemExit:
            pass  # continue on next file

upload_folder("notebooks", "notebooks")
upload_folder("converted", "converted")
