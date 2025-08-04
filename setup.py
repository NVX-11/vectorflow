#!/usr/bin/env python3
"""
Setup script for VectorFlow CLI
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="vectorflow-cli",
    version="1.0.0",
    author="VectorFlow Contributors",
    author_email="maintainers@vectorflow.dev",
    description="Fast, secure, local PDF ↔ Word document converter",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/vectorflow",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/vectorflow/issues",
        "Source": "https://github.com/yourusername/vectorflow",
        "Documentation": "https://github.com/yourusername/vectorflow/wiki",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Text Processing :: Markup",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
            "bandit>=1.7",
        ],
        "test": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "vectorflow=vectorflow:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "pdf", "word", "docx", "converter", "document", "conversion",
        "cli", "command-line", "privacy", "local", "offline"
    ],
    platforms=["any"],
)