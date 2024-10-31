***1. To install Python, follow these steps based on your operating system:***

***For Windows:***
Download the Installer:

Visit python.org.
Click on "Download Python" to get the latest version.
Run the Installer:

Open the downloaded .exe file.
During installation, check the box that says "Add Python to PATH" (this is crucial for using Python from the command line).
Select "Install Now" and follow the prompts.
Verify Installation:

Open Command Prompt (cmd) and type:
python --version
You should see the Python version number.


***For macOS:***
Using Homebrew (Recommended):

If you have Homebrew installed, you can install Python easily:
brew install python
Manual Download:
Go to python.org.
Download the latest .pkg installer for macOS.
Run the installer and follow the prompts.
Verify Installation:

Open Terminal and type:
python3 --version
You should see the Python version number.

***For Linux:***
Ubuntu/Debian:
sudo apt update
sudo apt install python3

***Fedora:***
sudo dnf install python3
Verify Installation:

In the terminal, type:
python3 --version


***2. To install Node.js, follow these steps based on your operating system:***

1. Using the Official Node.js Installer (All Platforms)
Download Node.js:

Go to the Node.js website.
Download the recommended version for most users (LTS) for stability, or the latest version if you need the newest features.
Run the Installer:

Open the downloaded file and run the installer.
Follow the prompts and accept the default settings.
Verify Installation:

Open a terminal (Command Prompt on Windows or Terminal on macOS/Linux) and type:
node --version
npm --version
You should see version numbers for both Node.js and npm.


***3. Install Flask and face_recognition***

pip install flask face_recognition flask-cors

If you see an error message saying "CMake is not installed on your system!" while trying to build or install a package, it means that your system lacks the cmake tool, which is often required for building software from source.

Here's how to install CMake on various platforms:

***On Ubuntu / Debian***
sudo apt update
sudo apt install cmake

***On Fedora***
sudo dnf install cmake

***On macOS (using Homebrew)***
If you have Homebrew installed:
brew install cmake

***On Windows***
Download the CMake installer from the official CMake website.
Run the installer and follow the instructions, making sure to add CMake to your system PATH during installation.


***4. Start the Flask server: python app.py***

update IMAGE_DIR = "/Users/your_username/Desktop/images_directory"  # Replace 'your_username' with your actual username(ex: mac os)

***5. Install nodejs http-server package to run static files locally***

npm install -g http-server

***6. start index.html:***
Go to folder and run "http-server"
