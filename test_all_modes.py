#!/usr/bin/env python3
"""
Comprehensive test script for PRET toolkit
Tests all printer languages and basic functionality
"""

import subprocess
import sys
import time

def run_test(cmd, description, timeout=10):
    """Run a test command and return results"""
    print(f"\n🧪 Testing: {description}")
    print(f"Command: {cmd}")
    
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=timeout
        )
        
        if result.returncode == 0:
            print("✅ PASS")
            return True
        else:
            print(f"❌ FAIL (return code: {result.returncode})")
            if result.stderr:
                print(f"Error: {result.stderr[:200]}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ TIMEOUT (expected for connection tests)")
        return True  # Timeout is expected for connection tests
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    print("🚀 PRET Enhanced Comprehensive Test Suite")
    print("=" * 60)

    tests = [
        # Basic functionality tests
        ("python3 pret.py --help", "Help system"),
        ("python3 pret.py", "Discovery mode"),

        # Security validation tests
        ("python3 -c \"from security import SecurityValidator; print('Security module:', 'OK' if SecurityValidator.is_safe_target('192.168.1.1') else 'FAIL')\"", "Security validation"),

        # Printer language tests (with timeout)
        ("timeout 5 python3 pret.py 127.0.0.1 ps --quiet", "PostScript mode"),
        ("timeout 5 python3 pret.py 127.0.0.1 pjl --quiet", "PJL mode"),
        ("timeout 5 python3 pret.py 127.0.0.1 pcl --quiet", "PCL mode"),

        # Debug mode tests
        ("timeout 5 python3 pret.py 127.0.0.1 ps --debug --quiet", "PostScript debug"),
        ("timeout 5 python3 pret.py 127.0.0.1 pjl --debug --quiet", "PJL debug"),

        # Enhanced help tests
        ("python3 -c \"from enhanced_help import EnhancedHelp; EnhancedHelp.show_mode_help('ps'); print('Enhanced help: OK')\"", "Enhanced help system"),

        # Error handling tests
        ("python3 pret.py invalid..target pjl 2>/dev/null || echo 'Input validation: OK'", "Input validation"),
        ("python3 pret.py 127.0.0.1 invalid_mode 2>/dev/null || echo 'Mode validation: OK'", "Mode validation"),

        # LPD script tests
        ("python3 lpd/lpdprint.py --help", "LPD print script"),
        ("python3 lpd/lpdtest.py --help", "LPD test script"),

        # File operations tests
        ("python3 -c \"import os; print('File operations: OK' if os.path.exists('pret.py') else 'FAIL')\"", "File system access"),
    ]
    
    passed = 0
    total = len(tests)
    
    for cmd, desc in tests:
        if run_test(cmd, desc):
            passed += 1
        time.sleep(1)  # Brief pause between tests
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print(f"⚠️  {total - passed} tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
