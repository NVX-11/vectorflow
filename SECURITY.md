# 🔒 Security Policy

- **Local Processing**: All conversions happen on your machine
- **No Data Collection**: Zero telemetry or analytics
- **Offline Operation**: No internet connection required
- **Open Source**: Full code transparency

##  Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ Yes    |
| < 1.0   | ❌ No     |


##  Security Best Practices

### For Users
```bash
# Keep updated
git pull origin main
pip install -r requirements.txt --upgrade

# Use virtual environments
python -m venv vectorflow-env
source vectorflow-env/bin/activate
```

### For Developers
```bash
# Check dependencies
pip audit

# Static analysis
bandit -r .
```

##  Known Limitations

- **Malicious PDFs**: Could exploit underlying libraries
- **File System Access**: Requires read/write permissions
- **Python Security**: Depends on Python installation security

##  Mitigation

- Only process trusted files
- Use sandboxed environments for untrusted content
- Keep Python and dependencies updated
