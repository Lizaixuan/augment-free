import os
import platform
import uuid


class Utils:

    @staticmethod
    def get_system() -> str:
        """Get the system name"""
        system = platform.system()
        return system

    @staticmethod
    def get_vscode_paths(system: str):
        """Get the VSCode directory paths"""
        paths = {}
        base_dir = None

        if system == "Windows":
            base_dir = os.path.join(os.environ["APPDATA"], "Code", "User")
        elif system == "Linux":
            base_dir = os.path.join(os.environ["HOME"], ".vscode", "User")
        elif system == "Darwin":
            base_dir = os.path.join(
                os.environ["HOME"], "Library", "Application Support", "Code", "User"
            )
        else:
            raise Exception("Unsupported system")

        # Check if directory exists
        if not os.path.exists(base_dir):
            raise Exception("VSCode not installed")

        paths["base_dir"] = base_dir  # VSCode user directory
        paths["storage_json"] = os.path.join(base_dir, "globalStorage", "storage.json")
        paths["state_db"] = os.path.join(base_dir, "globalStorage", "state.vscdb")

        return paths

    @staticmethod
    def generate_machine_id() -> str:
        """Generate a random 64-character hex string for machineId"""
        return uuid.uuid4().hex + uuid.uuid4().hex

    @staticmethod
    def generate_device_id() -> str:
        """Generate a random UUID v4 for devDeviceId"""
        return str(uuid.uuid4())
