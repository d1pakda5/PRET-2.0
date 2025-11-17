#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup script for PRET - Printer Exploitation Toolkit
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pret",
    version="0.40.1",
    author="Jens Müller, Enhanced by Community",
    author_email="jens.a.mueller@rub.de",
    description="Printer Exploitation Toolkit - Enhanced Python 3 Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/PRET",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "snmp": [
            "pysnmp>=4.4.0",
        ],
        "windows": [
            "win-unicode-console>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "pret=pret:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.dat", "*.eps", "*.ps", "*.pcl", "*.pfa"],
    },
    keywords="printer security testing exploitation postscript pjl pcl",
    project_urls={
        "Bug Reports": "https://github.com/your-username/PRET/issues",
        "Source": "https://github.com/your-username/PRET",
        "Documentation": "https://github.com/your-username/PRET/blob/main/README.md",
        "Security": "https://github.com/your-username/PRET/blob/main/SECURITY.md",
    },
)
