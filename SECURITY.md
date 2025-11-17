# Security Policy

## Supported Versions

We actively maintain and provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.40+   | ✅ Yes             |
| < 0.40  | ❌ No              |

## Security Enhancements in This Version

This enhanced version of PRET includes significant security improvements:

### Fixed Vulnerabilities

- **Code Injection (Critical)**: Fixed 19 instances of dangerous `eval(input())` calls that allowed arbitrary code execution
- **Path Traversal (High)**: Enhanced directory traversal protection with comprehensive path validation
- **Input Validation (Medium)**: Added comprehensive input sanitization and validation
- **Buffer Management (Low)**: Improved buffer handling and memory management

### New Security Features

- **Input Sanitization Module**: Comprehensive validation of all user inputs
- **Path Validation**: Secure file path handling with traversal prevention
- **Target Validation**: Hostname/IP validation to prevent injection attacks
- **Enhanced Error Handling**: Secure error messages without information disclosure

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability in PRET, please follow these steps:

### 1. Do Not Open a Public Issue

Please **DO NOT** report security vulnerabilities through public GitHub issues, discussions, or pull requests.

### 2. Contact Us Privately

Send details of the vulnerability to the project maintainers via:

- **Email**: [Create a private security advisory on GitHub]
- **GitHub Security Advisory**: Use GitHub's private vulnerability reporting feature

### 3. Provide Detailed Information

Include the following information in your report:

- **Description**: Clear description of the vulnerability
- **Impact**: Potential impact and attack scenarios
- **Reproduction**: Step-by-step instructions to reproduce the issue
- **Environment**: Python version, OS, and any relevant configuration
- **Proof of Concept**: Code or commands demonstrating the vulnerability (if applicable)

### 4. Response Timeline

We aim to respond to security reports within:

- **Initial Response**: 48 hours
- **Vulnerability Assessment**: 7 days
- **Fix Development**: 30 days (depending on complexity)
- **Public Disclosure**: After fix is released and users have time to update

## Security Best Practices for Users

### Authorized Use Only

PRET is designed for authorized security testing only:

- ✅ **DO**: Use on systems you own or have explicit permission to test
- ✅ **DO**: Follow responsible disclosure practices
- ✅ **DO**: Respect privacy and data protection laws
- ❌ **DON'T**: Use on systems without authorization
- ❌ **DON'T**: Use for malicious purposes
- ❌ **DON'T**: Access or modify data without permission

### Safe Testing Environment

- Use isolated test networks when possible
- Backup printer configurations before testing
- Monitor printer behavior during testing
- Have a rollback plan for any changes made

### Input Validation

When using PRET:

- Validate all file paths and names
- Use the `--safe` flag to verify language support
- Be cautious with file upload/download operations
- Monitor debug output for unexpected behavior

## Security Features

### Input Validation

```python
from security import SecurityValidator

# Validate targets
if SecurityValidator.is_safe_target(target):
    # Proceed with connection
    pass

# Sanitize filenames
clean_name = SecurityValidator.sanitize_filename(user_input)
```

### Path Protection

- Automatic path traversal detection and prevention
- Secure file operations with bounds checking
- Validation of all file system operations

### Connection Security

- Enhanced error handling for network operations
- Proper encoding/decoding of data streams
- Timeout management and resource cleanup

## Vulnerability Disclosure Timeline

When we receive a security report:

1. **Day 0**: Vulnerability reported
2. **Day 1-2**: Initial response and acknowledgment
3. **Day 3-7**: Vulnerability assessment and validation
4. **Day 8-30**: Fix development and testing
5. **Day 31+**: Coordinated disclosure and release

## Security Considerations for Developers

If you're contributing to PRET:

- Always validate user inputs
- Use parameterized queries and safe string handling
- Implement proper error handling without information disclosure
- Follow the principle of least privilege
- Add security tests for new features
- Review code for potential vulnerabilities

## Legal and Ethical Use

PRET is a security research tool intended for:

- Authorized penetration testing
- Security research and education
- Vulnerability assessment with proper authorization
- Compliance testing and auditing

**Unauthorized access to computer systems is illegal and unethical.**

## Contact

For security-related questions or concerns:

- Use GitHub's private vulnerability reporting
- Check existing security advisories
- Follow responsible disclosure practices

Thank you for helping keep PRET secure! 🔒
