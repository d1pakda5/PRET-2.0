#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Security utilities for PRET toolkit
Provides input validation and sanitization functions
"""

import re
import os
import string

class SecurityValidator:
    """Security validation and sanitization utilities"""
    
    # Allowed characters for filenames
    SAFE_FILENAME_CHARS = string.ascii_letters + string.digits + "._-"
    
    # Maximum lengths
    MAX_FILENAME_LENGTH = 255
    MAX_PATH_LENGTH = 4096
    MAX_COMMAND_LENGTH = 1024
    
    @staticmethod
    def sanitize_filename(filename):
        """Sanitize filename to prevent path traversal and injection"""
        if not filename:
            return ""
        
        # Remove path separators and dangerous characters
        filename = re.sub(r'[/\\<>:"|?*]', '_', filename)
        
        # Remove control characters
        filename = ''.join(c for c in filename if ord(c) >= 32)
        
        # Limit length
        if len(filename) > SecurityValidator.MAX_FILENAME_LENGTH:
            filename = filename[:SecurityValidator.MAX_FILENAME_LENGTH]
        
        # Ensure it's not empty after sanitization
        if not filename or filename in ['.', '..']:
            filename = 'sanitized_file'
        
        return filename
    
    @staticmethod
    def validate_path(path, base_dir=None):
        """Validate path to prevent directory traversal"""
        if not path:
            return False
        
        # Check length
        if len(path) > SecurityValidator.MAX_PATH_LENGTH:
            return False
        
        # Normalize path
        normalized = os.path.normpath(path)
        
        # Check for path traversal attempts
        if '..' in normalized or normalized.startswith('/'):
            return False
        
        # If base directory specified, ensure path stays within it
        if base_dir:
            try:
                full_path = os.path.join(base_dir, normalized)
                real_path = os.path.realpath(full_path)
                real_base = os.path.realpath(base_dir)
                return real_path.startswith(real_base)
            except (OSError, ValueError):
                return False
        
        return True
    
    @staticmethod
    def sanitize_command(command):
        """Sanitize command input to prevent injection"""
        if not command:
            return ""
        
        # Limit length
        if len(command) > SecurityValidator.MAX_COMMAND_LENGTH:
            command = command[:SecurityValidator.MAX_COMMAND_LENGTH]
        
        # Remove control characters except common ones
        allowed_control = ['\t', '\n', '\r']
        command = ''.join(c for c in command if ord(c) >= 32 or c in allowed_control)
        
        return command.strip()
    
    @staticmethod
    def is_safe_target(target):
        """Validate target hostname/IP to prevent injection"""
        if not target:
            return False
        
        # Basic validation for hostname/IP format
        # Allow alphanumeric, dots, hyphens, colons (for IPv6), and port numbers
        pattern = r'^[a-zA-Z0-9\.\-\:]+$'
        
        if not re.match(pattern, target):
            return False
        
        # Additional checks for common injection patterns
        dangerous_patterns = ['|', '&', ';', '`', '$', '(', ')', '{', '}', '[', ']']
        for pattern in dangerous_patterns:
            if pattern in target:
                return False
        
        return True
