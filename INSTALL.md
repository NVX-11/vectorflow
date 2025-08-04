# 🚀 VectorFlow Installation

##  Quick Install

```bash
git clone https://github.com/NVX-11/vectorflow.git
cd vectorflow
pip install -r requirements.txt
python vectorflow.py
```

##  Python Setup

### Windows
1. Download from [python.org](https://python.org/downloads/)
2. Check "Add Python to PATH" during installation
3. Verify: `python --version`

### macOS
```bash
# Using Homebrew
brew install python

# Verify
python3 --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

##  Installation Methods

### Method 1: Direct Install
```bash
pip install pdf2docx docx2pdf
python vectorflow.py
```

### Method 2: Virtual Environment (Recommended)
```bash
python -m venv vectorflow-env
source vectorflow-env/bin/activate  # Windows: vectorflow-env\Scripts\activate
pip install -r requirements.txt
python vectorflow.py
```

### Method 3: Download Script Only
```bash
curl -O https://raw.githubusercontent.com/NVX-11/vectorflow/vectorflow.py
pip install pdf2docx docx2pdf
python vectorflow.py
```

##  Verify Installation

```bash
# Check version
python vectorflow.py --version

# Test conversion
python vectorflow.py sample.pdf output.docx
```

##  Troubleshooting

### Permission Errors
```bash
# Use --user flag
pip install --user pdf2docx docx2pdf

# Or run as admin (Windows)
# Or use sudo (macOS/Linux)
```

### Network Issues
```bash
# Use different index
pip install -i https://pypi.org/simple/ pdf2docx docx2pdf
```

### Version Conflicts
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Force reinstall
pip install --force-reinstall pdf2docx docx2pdf
```

## 🔧 Requirements

- **Python**: 3.7+
- **OS**: Windows 10+, macOS 10.14+, Linux

##  Need Help?

- [User Guide](USER_GUIDE.md) - Detailed usage instructions
- [GitHub Issues](https://github.com/NVX-11/vectorflow/issues) - Technical support
- [Discussions](https://github.com/NVX-11/vectorflow/discussions) - Community help