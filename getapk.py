"""Put the package names of the apps you want the apks of extracted after the name of this script("getapk.py")."""
import os
import subprocess
import sys


ADB_PATH = r"adb path here"
DESTINATION = os.getcwd()
for package in sys.argv[1:]:
	packagePath = subprocess.run([ADB_PATH, "shell", "pm", "path", package], stdout=subprocess.PIPE).stdout.decode("utf-8").replace("package:", "").replace('\n', "")
	subprocess.run([ADB_PATH, "pull", packagePath, os.path.join(DESTINATION, package + ".apk")])