# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.40.1] - 2024-01-XX - Enhanced Python 3 Edition

### 🔒 Security
- **CRITICAL**: Fixed 19 instances of dangerous `eval(input())` calls that allowed arbitrary code execution
- **HIGH**: Enhanced path traversal protection with comprehensive validation
- **MEDIUM**: Added comprehensive input validation and sanitization
- **LOW**: Improved error handling to prevent information disclosure

### ✨ Added
- New `security.py` module with comprehensive input validation
- Enhanced help system (`enhanced_help.py`) with detailed command guides
- Comprehensive test suite (`test_all_modes.py`) with 14 automated tests
- Progress indicators with data transfer rates
- GitHub Actions workflow for automated testing
- Requirements.txt for easy dependency management
- Setup.py for proper Python package installation
- Contributing guidelines and security policy
- Enhanced documentation with examples and troubleshooting

### 🚀 Changed
- **BREAKING**: Converted entire codebase from Python 2 to Python 3.6+
- **BREAKING**: Removed dangerous `eval(input())` calls - may affect custom scripts
- Improved buffer management (8KB buffers for better performance)
- Enhanced error messages with actionable feedback
- Better connection handling with automatic reconnection
- Modernized argument parsing with proper validation
- Updated all documentation for Python 3

### 🐛 Fixed
- Fixed all Python 2/3 compatibility issues
- Corrected string/bytes handling throughout codebase
- Fixed print statement formatting issues
- Resolved import issues and deprecated warnings
- Fixed path traversal vulnerabilities
- Corrected encoding/decoding issues in network operations

### 🧪 Testing
- Added comprehensive test suite covering all functionality
- Security validation tests for input sanitization
- Performance benchmarks and reliability testing
- Real printer testing verification
- Automated syntax checking for all Python files

### 📚 Documentation
- Updated README with GitHub badges and quick start guide
- Added detailed enhancement documentation
- Created security policy and contributing guidelines
- Enhanced help system with mode-specific guides
- Added troubleshooting and best practices sections

### 🔧 Technical Improvements
- Enhanced connection management with better error handling
- Improved memory efficiency and resource cleanup
- Better timeout handling and watchdog mechanisms
- Optimized data processing and buffer management
- Enhanced logging and debug output formatting

## [0.40.0] - Original Release

### Added
- Initial PRET implementation
- PostScript, PJL, and PCL support
- Basic printer exploitation capabilities
- File system access and manipulation
- Network and USB connectivity
- Discovery functionality
- LPD testing scripts

---

## Migration Guide from v0.40.0 to v0.40.1

### Python Version
- **Old**: Python 2.7
- **New**: Python 3.6+
- **Action**: Update your Python installation

### Dependencies
- **Old**: Manual installation
- **New**: Use `pip3 install -r requirements.txt`
- **Action**: Install dependencies using requirements file

### Security Changes
- **Old**: `eval(input())` calls allowed arbitrary code execution
- **New**: Safe `input()` calls with validation
- **Action**: Review any custom scripts that relied on eval behavior

### Command Line
- **Old**: `python pret.py`
- **New**: `python3 pret.py`
- **Action**: Update scripts and documentation

### Testing
- **New**: Run `python3 test_all_modes.py` to verify functionality
- **Action**: Test your setup after migration

For detailed information about all changes, see [ENHANCEMENTS.md](ENHANCEMENTS.md).
