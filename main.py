#!/usr/bin/env python3
"""
SecureArch Portal - Main Entry Point for Executable
Cognizant SecArch Portal Web Application
"""

import sys
import os
import webbrowser
import threading
import time

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def open_browser():
    """Open the web browser after a short delay"""
    time.sleep(2)  # Wait for the server to start
    webbrowser.open('http://localhost:5000')

def main():
    """Main entry point for the SecureArch Portal"""
    print("🚀 Starting SecureArch Portal...")
    print("📊 Initializing Cognizant SecArch Portal Web Application")
    
    try:
        # Import the web application
        from app_web import app
        
        # Start browser in a separate thread
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        print("🌐 Server will start on http://localhost:5000")
        print("🔐 Demo Credentials:")
        print("   👤 User: admin@demo.com / password123")
        print("   🔍 Analyst: analyst@demo.com / analyst123")
        print("\n✨ Opening browser automatically...")
        print("\nPress Ctrl+C to stop the server")
        
        # Run the Flask application
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,  # Disable debug mode for production
            use_reloader=False  # Disable reloader for executable
        )
        
    except KeyboardInterrupt:
        print("\n👋 SecureArch Portal stopped by user")
    except Exception as e:
        print(f"❌ Error starting SecureArch Portal: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == '__main__':
    main() 