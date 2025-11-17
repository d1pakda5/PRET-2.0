# Contributing to PRET

Thank you for your interest in contributing to PRET! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Git
- Basic understanding of printer protocols (PostScript, PJL, PCL)

### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/PRET.git
   cd PRET
   ```

3. Install dependencies:
   ```bash
   pip3 install colorama pysnmp requests
   ```

4. Run the test suite to ensure everything works:
   ```bash
   python3 test_all_modes.py
   ```

## 🧪 Testing

Before submitting any changes, please ensure:

1. All existing tests pass:
   ```bash
   python3 test_all_modes.py
   ```

2. Your code follows Python 3 best practices
3. New features include appropriate tests
4. Security considerations are addressed

## 📝 Submitting Changes

### Pull Request Process

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request on GitHub

### Commit Message Guidelines

- Use clear, descriptive commit messages
- Start with a verb in present tense (e.g., "Add", "Fix", "Update")
- Keep the first line under 50 characters
- Include details in the body if necessary

Example:
```
Fix buffer overflow in PJL parser

- Validate input length before processing
- Add bounds checking for command parameters
- Update tests to cover edge cases
```

## 🔒 Security Guidelines

### Reporting Security Issues

If you discover a security vulnerability, please:

1. **DO NOT** open a public issue
2. Email the maintainers privately
3. Provide detailed information about the vulnerability
4. Allow time for the issue to be addressed before public disclosure

### Security Best Practices

When contributing code:

- Validate all user inputs
- Use safe string handling practices
- Avoid `eval()` and similar dangerous functions
- Implement proper error handling
- Follow the principle of least privilege

## 📋 Code Style

### Python Style Guidelines

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Example:

```python
def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to prevent path traversal attacks.
    
    Args:
        filename: The filename to sanitize
        
    Returns:
        A sanitized filename safe for file operations
    """
    if not filename:
        return ""
    
    # Remove dangerous characters
    filename = re.sub(r'[/\\<>:"|?*]', '_', filename)
    return filename
```

## 🐛 Bug Reports

When reporting bugs, please include:

- Python version
- Operating system
- Steps to reproduce the issue
- Expected vs actual behavior
- Any error messages or logs
- Printer model/type if relevant

## 💡 Feature Requests

For new features:

- Explain the use case and benefits
- Provide examples of how it would work
- Consider security implications
- Discuss implementation approach

## 📚 Documentation

Help improve documentation by:

- Fixing typos and grammar
- Adding examples and use cases
- Improving clarity and organization
- Updating outdated information

## 🤝 Community Guidelines

- Be respectful and inclusive
- Help others learn and grow
- Focus on constructive feedback
- Follow responsible disclosure for security issues
- Remember this tool is for authorized testing only

## 📞 Getting Help

- Check existing issues and documentation first
- Ask questions in GitHub Discussions
- Be specific about your problem
- Provide relevant context and details

Thank you for contributing to PRET! 🖨️🔓
