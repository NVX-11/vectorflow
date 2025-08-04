# 🤝 Contributing to VectorFlow

##  Quick Start

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/NVX-11/vectorflow.git`
3. **Create** a branch: `git checkout -b feature/your-feature`
4. **Make** your changes
5. **Test** your changes: `python vectorflow.py`
6. **Commit**: `git commit -m "Add your feature"`
7. **Push**: `git push origin feature/your-feature`
8. **Create** a Pull Request

##  Bug Reports

**Before submitting:**
- Search existing issues
- Test with latest version
- Include system info (OS, Python version)

**Include in your report:**
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Error messages/screenshots

##  Feature Requests

**Good feature requests include:**
- Clear problem statement
- Proposed solution
- Use cases

##  Development Setup

```bash
# Clone and setup
git clone https://github.com/NVX-11/vectorflow.git
cd vectorflow
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Test your changes
python vectorflow.py --version
python vectorflow.py sample.pdf output.docx
```

##  Code Style

- Follow PEP 8
- Add docstrings for functions
- Use type hints where possible
- Handle exceptions gracefully

```python
def convert_pdf_to_word(input_path: str, output_path: str) -> bool:
    """Convert PDF to Word document.
    
    Args:
        input_path: Path to input PDF
        output_path: Path to output Word file
        
    Returns:
        True if successful, False otherwise
    """
```

##  Testing

```bash
# Test basic functionality
python vectorflow.py sample.pdf test.docx
python vectorflow.py test.docx test.pdf

# Test error handling
python vectorflow.py nonexistent.pdf output.docx
```

##  Pull Request Checklist

- [ ] Code follows style guidelines
- [ ] Changes tested locally
- [ ] Documentation updated (if needed)
- [ ] Commit messages are clear
- [ ] No new warnings/errors


##  Questions?

- [GitHub Discussions](https://github.com/NVX-11/vectorflow/discussions)
- [Issues](https://github.com/NVX-11/vectorflow/issues)

Thanks for contributing! 🎉