from google_drive_downloader import GoogleDriveDownloader as gdd
import sys
import os
import requests


def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform
    
    return platforms[sys.platform]

platform = get_platform()

if platform == "linux":
    print("Nothing needs to install")
else:
    print("Installing ffmpeg")
    gdd.download_file_from_google_drive(file_id='1Q5zbaXonPEUNQmclp1WMIVVodnUuJdKo',
                                    dest_path='./ffmpeg.exe',
                                    unzip=False)