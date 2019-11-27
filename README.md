# Set Python - Selenium automation environment 

This document is based on Windows experience, other OS should require similar steps.

- First download Python 2.7 (latest version) from here if you still don’t have it: https://www.python.org/downloads/ and Install (for Mac “ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" )
- Add to PATH system environment variable the following routes: ‘C:\Python27’; ‘C:\Python27\Scripts’
- Download and install git from https://git-scm.com/downloads
- Download get-pip.py from https://github.com/pypa/get-pip can download the zip file and install it manually (on macOS:  sudo easy_install pip)
- Create a folder with your project name in the root directory (C:)
- Go to the github repository () and copy the .git path to clipboard
- Open CMD or Git Bash console, go to ‘C:\’ and type ‘git clone ‘ and then paste the path from your clipboard. This will download the repository in your local machine.
- Standing on ‘C:\your_project_name’ with Git Bash type ‘pip install -r requirements.txt’. 
- Install selenium and pyperclip libs (pip install selenium and then the same with pyperclip)
- Type “pip list” and it will display all libraries installed.
- Go to “C:\your_project_name\tests” with the console and there you can run tests with the following command: “python -m pytest” or you run an specific test with “python -m pytest  test_whatever_the_test_name_be.py”
- If you get an error that some library is missing just type “pip install missing_library_name”.
