import os
import shutil
import platform
import subprocess

def clean_temporary_files():
    # Clean temporary files based on the OS
    if platform.system() == "Windows":
        os.system("del /f /q %temp%\*")
        print("Temporary files cleaned on Windows.")
    elif platform.system() == "Linux":
        os.system("sudo rm -rf /tmp/*")
        print("Temporary files cleaned on Linux.")
    elif platform.system() == "Darwin":
        os.system("sudo rm -rf /private/tmp/*")
        print("Temporary files cleaned on macOS.")

def optimize_disk_space():
    # Remove unnecessary files to optimize disk space
    if platform.system() == "Windows":
        os.system("cleanmgr /sagerun:1")  # Run Disk Cleanup utility
        print("Disk space optimized on Windows.")
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "apt", "autoclean"])  # Clean apt cache
        print("Disk space optimized on Linux.")
    elif platform.system() == "Darwin":
        os.system("sudo rm -rf /Library/Caches/*")  # Clear macOS cache
        print("Disk space optimized on macOS.")

def check_system_updates():
    # Check for system updates
    if platform.system() == "Windows":
        os.system("wuauclt /detectnow /updatenow")  # Check for Windows updates
        print("Checking for system updates on Windows.")
    elif platform.system() == "Linux":
        subprocess.run(["sudo", "apt", "update"])  # Update package lists
        subprocess.run(["sudo", "apt", "upgrade", "-y"])  # Upgrade installed packages
        print("Checking for system updates on Linux.")
    elif platform.system() == "Darwin":
        os.system("softwareupdate -l")  # List available macOS updates
        print("Checking for system updates on macOS.")

if __name__ == "__main__":
    print("Starting system maintenance tasks...")
    clean_temporary_files()
    optimize_disk_space()
    check_system_updates()
    print("System maintenance tasks completed.")
