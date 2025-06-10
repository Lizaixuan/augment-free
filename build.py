import os
import platform
import subprocess
import shutil


def build_executable():
    """Build executables for the current platform"""
    system = platform.system()
    print(f"Building for {system}...")

    # Clean previous builds
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")

    # Base command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--clean",
        "--name",
        f"AugmentFree-{system.lower()}",
        "main.py",
    ]

    # Run PyInstaller
    subprocess.run(cmd)

    print(f"Build completed for {system}. Executable is in the 'dist' folder.")


if __name__ == "__main__":
    build_executable()
