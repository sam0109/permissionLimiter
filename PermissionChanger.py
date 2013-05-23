#!/usr/bin/python
import subprocess
import os
import re

def readPermissions():
	permission = {}
	subprocess.call("apktool d -f ./TestApp.apk", shell=True)
	manifest = open( "./TestApp/AndroidManifest.xml")
	j=0
	for line in manifest:
		if re.search('<uses-permission android:name=', line):
			line = re.sub('<uses-permission android:name="android.permission\.','',line)
			line = re.sub('" />\n$','',line)
			permission[j] = line
		j += 1
	return permission
permission = readPermissions()
print '\npermissions currently in the .apk file in this directory:\n'
i = 0
for value in permission:
	print value + permission
removePermission = input('permissions to remove (sparated by commas, e.g. "1,5,12"):')
print ('removing '+str(removePermission))
