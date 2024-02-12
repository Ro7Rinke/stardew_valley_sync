import subprocess
import atexit
import zipfile
import os
import time
import platform
import shutil
# import urllib.request
import requests
# import gzip

def runSoftware():
    try:
        softwareProcess = subprocess.call(["/usr/bin/open", "-W", "-n", "-a", "/Applications/Poker.app"])

        atexit.register(onExit, softwareProcess)
        
    except Exception as e:
        print(f"Error: {e}")

def onExit(softwareProcess):
    originalSavePath = getSavePath()
    savePath = './StardewValley'

    copy_folder(originalSavePath, savePath)

    # savePath = getSavePath

    timestamp = time.time()
    backupFileName = 'StardewValley' + str(timestamp) + '.zip'
    backupFilePath = './' + backupFileName
    
    zipFolder(savePath, backupFilePath)

    uploadFile(backupFilePath)

def getSavePath():
    systemPlatform = platform.system()

    savePath = ''
    if systemPlatform == "Windows":
        savePath = './test'
    elif systemPlatform == "Darwin":
        savePath = '/Users/ro7rinke/.config/StardewValley'
    elif systemPlatform == "Linux":
        savePath = './test'
    else:
        raise ValueError("Operating system is not Windows, macOS, or Linux")
    
    return savePath

def zipFolder(input_folder, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_folder)
                zipf.write(file_path, arcname=arcname)

def uploadFile(filePath):
    url = 'http://localhost:8000/upload/'

    # with open(filePath, 'rb') as file:
    #     fileData = file.read()

    #     req = urllib.request.Request(url, data=fileData, method='POST')
    #     req.add_header('Content-Type', 'application/octet-stream')
    #     req.add_header('Content-Length', len(fileData))

    #     with urllib.request.urlopen(req) as response:
    #         if response.getcode() == 201:
    #             print('File uploaded successfully!')
    #         else:
    #             print('Error uploading file:', response.getcode())

    files = {'file': open(filePath, 'rb')}

    response = requests.post(url, files=files)

    if response.status_code == 201:
        print('File uploaded successfully!')
    else:
        print('Error uploading file:', response.status_code)

def copy_folder(source_folder, destination_folder):
    try:
        shutil.copytree(source_folder, destination_folder)
        # print(f"Folder '{source_folder}' copied to '{destination_folder}' successfully.")
    except shutil.Error as e:
        print(f"Error copying folder: {e}")

if __name__ == "__main__":
    runSoftware()

# def zip_and_compress_folder(input_folder, output_archive):
#     # Step 1: Zip the folder
#     shutil.make_archive(output_archive, 'zip', input_folder)

#     # Step 2: Compress the zip file using gzip
#     with open(f"{output_archive}.zip", 'rb') as f_in, gzip.open(f"{output_archive}.gz", 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

#     # Step 3: Remove the original zip file
#     os.remove(f"{output_archive}.zip")