#!/usr/bin/env python3
"""
Test script to verify AuraDent Bot setup
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test if all required packages can be imported"""
    try:
        import telegram
        print("✅ python-telegram-bot imported successfully")
        
        import openpyxl
        print("✅ openpyxl imported successfully")
        
        import dotenv
        print("✅ python-dotenv imported successfully")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_file_structure():
    """Test if all required files exist"""
    required_files = [
        'bot.py',
        'requirements.txt',
        '.env.example',
        'README.md',
        '.gitignore',
        '.github/copilot-instructions.md'
    ]
    
    all_exist = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} missing")
            all_exist = False
    
    return all_exist

def test_bot_syntax():
    """Test if bot.py has valid syntax"""
    try:
        with open('bot.py', 'r', encoding='utf-8') as f:
            code = f.read()
        
        compile(code, 'bot.py', 'exec')
        print("✅ bot.py syntax is valid")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error in bot.py: {e}")
        return False
    except Exception as e:
        print(f"❌ Error checking bot.py: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing AuraDent Bot Setup")
    print("=" * 40)
    
    print("\n📦 Testing Package Imports:")
    imports_ok = test_imports()
    
    print("\n📁 Testing File Structure:")
    files_ok = test_file_structure()
    
    print("\n🐍 Testing Python Syntax:")
    syntax_ok = test_bot_syntax()
    
    print("\n" + "=" * 40)
    if imports_ok and files_ok and syntax_ok:
        print("🎉 All tests passed! Your AuraDent Bot is ready to run.")
        print("\n📋 Next steps:")
        print("1. Copy .env.example to .env")
        print("2. Configure your BOT_TOKEN and ADMIN_CHAT_ID in .env")
        print("3. Run: python bot.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == '__main__':
    main()