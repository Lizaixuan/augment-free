import json

from printer import Printer
from utils import Utils


class Storage:

    def __init__(self, file_path: str, printer: Printer):
        self.file_path = file_path
        self.printer = printer

    def read_storage_json(self):
        """Read the storage.json file"""
        with open(self.file_path, "r") as f:
            return json.load(f)

    def backup_file(self) -> str:
        """
        Create a backup of a file by adding '.bak' suffix to the original file name.
        The backup is created in the same directory as the original file.

        Args:
            file_path: Path to the file to backup

        Returns:
            str: Path to the backup file
        """
        import shutil

        # Create backup path by adding .bak suffix
        backup_path = self.file_path + ".bak"

        # Create the backup
        shutil.copy2(self.file_path, backup_path)

        return backup_path

    def reset(self):
        """Reset the sqmId and machineId in the storage.json file"""

        # Backup the original file
        backup_path = self.backup_file()
        self.printer.success(f"Backup storage.json to: {backup_path}")

        # Read the original file
        data = self.read_storage_json()

        # Reset the sqmId and machineId
        sqmId = Utils.generate_device_id()
        machineId = Utils.generate_machine_id()
        devDeviceId = Utils.generate_device_id()

        self.printer.info(f"Generated sqmId: {sqmId}")
        self.printer.info(f"Generated machineId: {machineId}")
        self.printer.info(f"Generated devDeviceId: {devDeviceId}")

        data["telemetry.sqmId"] = sqmId
        data["telemetry.machineId"] = machineId
        data["telemetry.devDeviceId"] = devDeviceId

        # Write the updated data to the original file
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

        self.printer.success("Reset storage.json")
