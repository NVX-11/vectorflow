# 📖 VectorFlow User Guide

##  Usage

### Interactive Mode
```bash
python vectorflow.py
```
Follow the prompts to select input and output files.

### Command Line
```bash
# PDF to Word
python vectorflow.py document.pdf document.docx

# Word to PDF  
python vectorflow.py document.docx document.pdf

# Auto-detect output format
python vectorflow.py document.pdf  # Creates document.docx
```

##  Supported Formats

| Input | Output | Status |
|-------|--------|--------|
| PDF | DOCX | ✅ Supported |
| DOCX | PDF | ✅ Supported |
| DOC | PDF | ✅ Supported |

##  Troubleshooting

### Common Issues

**"Library not found" Error**
```bash
pip install pdf2docx docx2pdf
```

**"File not found" Error**
- Check file path is correct
- Use quotes for paths with spaces: `"My Document.pdf"`

**Permission Errors**
```bash
# Windows: Run as Administrator
# macOS/Linux: 
sudo python vectorflow.py
```
