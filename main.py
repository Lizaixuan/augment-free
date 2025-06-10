import sys
from logo import print_logo
from printer import Printer
from state_db import StateDB
from storage import Storage
from utils import Utils

printer = Printer()


def main():
    # Print logo
    print_logo()

    # Get system information
    system = Utils.get_system()
    printer.info(f"Current operating system: {system}")

    # Get VSCode paths
    vscode_paths = Utils.get_vscode_paths(system)
    for name, path in vscode_paths.items():
        printer.info(f"Found {name} path: {path}")

    # Reset storage.json
    storage = Storage(vscode_paths["storage_json"], printer)
    storage.reset()

    # Reset state.vsdb
    state_db = StateDB(vscode_paths["state_db"], printer)
    state_db.reset()

    printer.success("VSCode-Augment environment reset completed")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        printer.error(f"An error occurred: {e}")
    finally:
        input("\nPress any key to exit...")
        sys.exit(0)  # Changed from 1 to 0 for successful exit
