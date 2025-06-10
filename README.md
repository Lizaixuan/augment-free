
[English](README.md) | [简体中文](README.zh-CN.md)

![AugmentFree Logo](/image/logo.png)

AugmentFree is a utility tool designed to reset the VSCode-Augment environment. It helps you clean up the Augment extension state when you encounter issues with the Augment AI assistant in VSCode.

> **Disclaimer**: This code is provided for learning purposes only. Use at your own risk.

## Features

- Resets the Augment extension storage file
- Clears the Augment state database
- Works across different operating systems (Windows, macOS, Linux)
- Simple command-line interface

## Requirements

- Python 3.8 or higher
- VSCode with Augment extension installed

> **Note**: This tool only supports the VSCode version of Augment. It does not work with other IDE integrations.

## Installation

### Clone the repository

```bash
git clone https://github.com/Lizaixuan/AugmentFree.git
# or
git clone https://gitee.com/BenLi19999/augment-free.git

cd AugmentFree
```

### Set up the environment

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Using Python

Run the tool with Python:

```bash
python main.py
```

## Building Executables

To build the executables yourself:

```bash
# Run the build script
python build.py
```

This will create an executable for your current platform in the `dist` directory.

The tool will:
1. Detect your operating system
2. Find the VSCode-Augment configuration paths
3. Reset the storage.json file
4. Reset the state.vsdb database
5. Confirm successful reset

## When to Use

Use AugmentFree when:
- Augment AI assistant is not responding correctly
- You're experiencing authentication issues with Augment
- The extension state seems corrupted
- You want to start with a clean Augment environment

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Zayn

## Links

- GitHub: [https://github.com/Lizaixuan/AugmentFree](https://github.com/Lizaixuan/AugmentFree)
- Gitee: [https://gitee.com/BenLi19999/augment-free](https://gitee.com/BenLi19999/augment-free)
