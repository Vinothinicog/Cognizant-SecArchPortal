===============================================================================
                    COGNIZANT SECUREARCH PORTAL - STANDALONE EXECUTABLE
===============================================================================

OVERVIEW
--------
This is a standalone executable version of the Cognizant SecureArch Portal.
No installation or Python environment setup is required. Simply run the 
executable file to start the application.

FILES INCLUDED
--------------
- SecureArchPortal.exe          : Main application executable
- Start_SecureArch_Portal.bat   : Convenient startup script
- README_EXECUTABLE.txt         : This file

HOW TO RUN
----------
Option 1: Double-click "Start_SecureArch_Portal.bat" for guided startup
Option 2: Double-click "SecureArchPortal.exe" directly
Option 3: Run from command line: .\SecureArchPortal.exe

WHAT HAPPENS WHEN YOU RUN IT
----------------------------
1. The application starts a web server on your local machine
2. Your default web browser opens automatically
3. The application is accessible at: http://localhost:5000
4. All data is stored locally in an embedded database

DEMO CREDENTIALS
----------------
User Account:
  Email: admin@demo.com
  Password: password123

Analyst Account:
  Email: analyst@demo.com
  Password: analyst123

FEATURES
--------
✅ Split Security Review Categories:
   - Application Security Review (14 OWASP categories)
   - Cloud Security Review (AWS, Azure, GCP)

✅ Complete Security Assessment Workflow:
   - Application onboarding
   - Security questionnaires
   - Combined review results
   - STRIDE threat analysis

✅ Analyst Dashboard:
   - Review submitted assessments
   - Add STRIDE findings
   - Manage security reviews

SYSTEM REQUIREMENTS
-------------------
- Windows 10/11 (64-bit)
- No additional software installation required
- Approximately 25MB disk space
- Available network port 5000

TROUBLESHOOTING
---------------
Issue: Port 5000 already in use
Solution: Close other applications using port 5000, or restart your computer

Issue: Antivirus blocking the executable
Solution: Add the executable to your antivirus whitelist

Issue: Browser doesn't open automatically
Solution: Manually navigate to http://localhost:5000

STOPPING THE APPLICATION
------------------------
- Press Ctrl+C in the command window
- Or simply close the command window

DATA STORAGE
------------
- All application data is stored in a local SQLite database
- Data persists between application runs
- Database file is included with the executable

SECURITY NOTES
--------------
- This is a development/demo version
- Not intended for production use
- Run only on trusted networks
- Database contains demo data

SUPPORT
-------
For technical support or questions about the SecureArch Portal,
please contact your Cognizant representative.

VERSION INFORMATION
-------------------
Application: SecureArch Portal
Version: 1.0 (Standalone Executable)
Build Date: August 2025
Platform: Windows x64

===============================================================================
                            © 2025 Cognizant Technology Solutions
=============================================================================== 