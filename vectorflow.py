#!/usr/bin/env python3
"""
VectorFlow CLI - Fast PDF/Word Document Converter
A lightweight tool for converting between PDF and Word formats.
"""

import os
import sys
import argparse
from pathlib import Path

# ASCII Art Logo
LOGO = """
██╗   ██╗███████╗ ██████╗████████╗ ██████╗ ██████╗ ███████╗██╗      ██████╗ ██╗    ██╗
██║   ██║██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██║     ██╔═══██╗██║    ██║
██║   ██║█████╗  ██║        ██║   ██║   ██║██████╔╝█████╗  ██║     ██║   ██║██║ █╗ ██║
╚██╗ ██╔╝██╔══╝  ██║        ██║   ██║   ██║██╔══██╗██╔══╝  ██║     ██║   ██║██║███╗██║
 ╚████╔╝ ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║██║     ███████╗╚██████╔╝╚███╔███╔╝
  ╚═══╝  ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝  ╚══╝╚══╝
"""

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_logo():
    """Print the VectorFlow logo with golden gradient colors"""
    lines = LOGO.strip().split('\n')
    # Golden/orange gradient colors to match the reference image
    colors = [Colors.YELLOW, '\033[38;5;220m', '\033[38;5;214m', '\033[38;5;208m', '\033[38;5;202m', '\033[38;5;196m']
    
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        print(f"{color}{line}{Colors.ENDC}")

def print_tips():
    """Print usage tips"""
    print(f"\n{Colors.GRAY}Tips for getting started:")
    print(f"1. Convert PDF to Word: vectorflow input.pdf output.docx")
    print(f"2. Convert Word to PDF: vectorflow input.docx output.pdf")
    print(f"3. Use --help for more information.{Colors.ENDC}\n")

def show_progress(message, color=Colors.CYAN):
    """Show a progress message"""
    print(f"{color}• {message}{Colors.ENDC}")

def convert_pdf_to_word(input_path, output_path):
    """Convert PDF to Word document"""
    try:
        import pdf2docx
        show_progress(f"Converting {input_path} to Word format...")
        
        # Convert PDF to Word
        cv = pdf2docx.Converter(input_path)
        cv.convert(output_path, start=0, end=None)
        cv.close()
        
        show_progress(f"✓ Successfully converted to {output_path}", Colors.GREEN)
        return True
        
    except ImportError:
        print(f"{Colors.RED}Error: pdf2docx library not found. Install with: pip install pdf2docx{Colors.ENDC}")
        return False
    except Exception as e:
        print(f"{Colors.RED}Error converting PDF to Word: {str(e)}{Colors.ENDC}")
        return False

def convert_word_to_pdf(input_path, output_path):
    """Convert Word document to PDF"""
    try:
        import docx2pdf
        show_progress(f"Converting {input_path} to PDF format...")
        
        # Convert Word to PDF
        docx2pdf.convert(input_path, output_path)
        
        show_progress(f"✓ Successfully converted to {output_path}", Colors.GREEN)
        return True
        
    except ImportError:
        print(f"{Colors.RED}Error: docx2pdf library not found. Install with: pip install docx2pdf{Colors.ENDC}")
        return False
    except Exception as e:
        print(f"{Colors.RED}Error converting Word to PDF: {str(e)}{Colors.ENDC}")
        return False

def detect_conversion_type(input_file, output_file):
    """Detect the type of conversion needed based on file extensions"""
    input_ext = Path(input_file).suffix.lower()
    output_ext = Path(output_file).suffix.lower()
    
    if input_ext == '.pdf' and output_ext in ['.docx', '.doc']:
        return 'pdf_to_word'
    elif input_ext in ['.docx', '.doc'] and output_ext == '.pdf':
        return 'word_to_pdf'
    else:
        return None

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='VectorFlow - Fast PDF/Word Document Converter',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('input', nargs='?', help='Input file path')
    parser.add_argument('output', nargs='?', help='Output file path')
    parser.add_argument('--version', action='version', version='VectorFlow 1.0.0')
    
    args = parser.parse_args()
    
    # Print logo and tips if no arguments
    if not args.input:
        print_logo()
        print_tips()
        
        # Interactive mode
        try:
            input_file = input(f"{Colors.CYAN}> Enter input file path: {Colors.ENDC}").strip()
            if not input_file:
                print(f"{Colors.YELLOW}No input file provided. Exiting.{Colors.ENDC}")
                return
            
            output_file = input(f"{Colors.CYAN}> Enter output file path: {Colors.ENDC}").strip()
            if not output_file:
                print(f"{Colors.YELLOW}No output file provided. Exiting.{Colors.ENDC}")
                return
                
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Operation cancelled.{Colors.ENDC}")
            return
    else:
        input_file = args.input
        output_file = args.output
    
    # Validate input file exists
    if not os.path.exists(input_file):
        print(f"{Colors.RED}Error: Input file '{input_file}' not found.{Colors.ENDC}")
        return
    
    # Auto-generate output filename if not provided
    if not output_file:
        input_path = Path(input_file)
        if input_path.suffix.lower() == '.pdf':
            output_file = str(input_path.with_suffix('.docx'))
        elif input_path.suffix.lower() in ['.docx', '.doc']:
            output_file = str(input_path.with_suffix('.pdf'))
        else:
            print(f"{Colors.RED}Error: Unsupported input file format. Use PDF or Word documents.{Colors.ENDC}")
            return
    
    # Detect conversion type
    conversion_type = detect_conversion_type(input_file, output_file)
    
    if not conversion_type:
        print(f"{Colors.RED}Error: Invalid conversion. Supported: PDF ↔ Word (.docx){Colors.ENDC}")
        return
    
    print(f"\n{Colors.BOLD}🚀 VectorFlow Converter{Colors.ENDC}")
    print(f"{Colors.GRAY}Input:  {input_file}{Colors.ENDC}")
    print(f"{Colors.GRAY}Output: {output_file}{Colors.ENDC}")
    print()
    
    # Perform conversion
    success = False
    if conversion_type == 'pdf_to_word':
        success = convert_pdf_to_word(input_file, output_file)
    elif conversion_type == 'word_to_pdf':
        success = convert_word_to_pdf(input_file, output_file)
    
    if success:
        file_size = os.path.getsize(output_file)
        print(f"{Colors.GREEN}✓ Conversion completed! Output size: {file_size:,} bytes{Colors.ENDC}")
    else:
        print(f"{Colors.RED}✗ Conversion failed.{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()