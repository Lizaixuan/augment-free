import os
from dotenv import load_dotenv
from rich import print

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Build the full path to the .env file
env_path = os.path.join(current_dir, ".env")

# Load environment variables, specifying the .env file path
load_dotenv(env_path)

# Get the version number, using the default value if not found
version = os.getenv("version", "0.1.0")
augment_version = os.getenv("augment_version", "0.1.0")

LOGO_TEXT = f"""
 █████╗ ██╗   ██╗ ██████╗ ███╗   ███╗███████╗███╗  ██╗████████╗  ███████╗██████╗ ███████╗███████╗
██╔══██╗██║   ██║██╔════╝ ████╗ ████║██╔════╝████╗ ██║╚══██╔══╝  ██╔════╝██╔══██╗██╔════╝██╔════╝
███████║██║   ██║██║  ██╗ ██╔████╔██║█████╗  ██╔██╗██║   ██║     █████╗  ██████╔╝█████╗  █████╗  
██╔══██║██║   ██║██║  ╚██╗██║╚██╔╝██║██╔══╝  ██║╚████║   ██║     ██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  
██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚███║   ██║     ██║     ██║  ██║███████╗███████╗
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚══╝   ╚═╝     ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
"""

DESCRIPTION_TEXT = f"""
AugmentFree v{version} | vscode-augment v{augment_version}  
Environment Reset Tool · Author: Zayn
"""

OTHER_INFO_TEXT = f"""
Github: https://github.com/Lizaixuan/augment-free
Gitee: https://gitee.com/BenLi19999/augment-free
"""


def print_logo():
    print(f"[#f19102]{LOGO_TEXT}[/#f19102]")
    print(f"[#3d855e]{DESCRIPTION_TEXT}[/#3d855e]")
    print(f"[#ff5722]{OTHER_INFO_TEXT}[/#ff5722]")


if __name__ == "__main__":
    print_logo()
