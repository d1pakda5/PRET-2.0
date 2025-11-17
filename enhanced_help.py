#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Enhanced help system for PRET toolkit
Provides detailed help, examples, and usage guidance
"""

class EnhancedHelp:
    """Enhanced help system with examples and detailed explanations"""
    
    @staticmethod
    def show_welcome():
        """Show enhanced welcome message with quick start guide"""
        print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    PRET - Printer Exploitation Toolkit v0.40                ║
║                          Enhanced Python 3 Edition                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Quick Start:                                                                ║
║    python3 pret.py                          # Discover printers             ║
║    python3 pret.py <target> <mode>          # Connect to printer            ║
║    python3 pret.py <target> <mode> --help   # Show mode-specific help       ║
║                                                                              ║
║  Modes:                                                                      ║
║    ps   - PostScript mode (most printers)                                   ║
║    pjl  - PJL mode (HP and compatible)                                      ║
║    pcl  - PCL mode (HP and compatible)                                      ║
║                                                                              ║
║  Examples:                                                                   ║
║    python3 pret.py 192.168.1.100 ps         # PostScript mode              ║
║    python3 pret.py printer.local pjl --debug # PJL with debug output       ║
║    python3 pret.py /dev/usb/lp0 pcl         # USB printer                   ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """)
    
    @staticmethod
    def show_mode_help(mode):
        """Show mode-specific help and commands"""
        if mode == 'ps':
            print("""
PostScript Mode Commands:
  id                    - Get device information
  version              - Get PostScript version
  devices              - List available devices
  ls [path]            - List directory contents
  get <file>           - Download file
  put <file>           - Upload file
  cd <path>            - Change directory
  pwd                  - Show current directory
  df                   - Show disk usage
  disable <feature>    - Disable PostScript feature
  enable <feature>     - Enable PostScript feature
  restart              - Restart PostScript interpreter
  reset                - Reset device
            """)
        elif mode == 'pjl':
            print("""
PJL Mode Commands:
  info <category>      - Get device information
  set <var>=<value>    - Set PJL variable
  echo <text>          - Echo text
  ls [path]            - List directory contents
  get <file>           - Download file
  put <file>           - Upload file
  cd <path>            - Change directory
  pwd                  - Show current directory
  df                   - Show disk usage
  format               - Format file system
  lock                 - Lock control panel
  unlock               - Unlock control panel
  reset                - Reset device
            """)
        elif mode == 'pcl':
            print("""
PCL Mode Commands:
  selftest             - Print self-test page
  info                 - Get device information
  fonts                - List available fonts
  macros               - List stored macros
  reset                - Reset device
  enter                - Enter PCL mode
  exit                 - Exit PCL mode
            """)
    
    @staticmethod
    def show_security_tips():
        """Show security testing tips and best practices"""
        print("""
Security Testing Tips:
  
  1. Always get proper authorization before testing
  2. Test in isolated environments when possible
  3. Document all findings and vulnerabilities
  4. Use --safe flag to verify language support first
  5. Monitor printer behavior during testing
  6. Be aware that some commands may affect printer operation
  
  Common Security Tests:
  - File system access (ls, get, put)
  - Information disclosure (info, version, id)
  - Configuration changes (set variables)
  - Denial of service (reset, format)
  - Memory access (PostScript operators)
        """)
    
    @staticmethod
    def show_troubleshooting():
        """Show common troubleshooting tips"""
        print("""
Troubleshooting:
  
  Connection Issues:
  - Verify printer IP/hostname is correct
  - Check if printer is powered on and connected
  - Try different ports (9100, 515, 631)
  - Use --debug flag to see network traffic
  
  Command Issues:
  - Use 'help' command in interactive mode
  - Try --safe flag to check language support
  - Increase timeout with 'timeout <seconds>'
  - Some printers may not support all commands
  
  Performance Issues:
  - Use --quiet flag to reduce output
  - Increase timeout for slow printers
  - Consider network latency and printer speed
        """)
