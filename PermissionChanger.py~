#!/usr/bin/python
import subprocess
import os
import re

def replace_line(file_name, line_num, text):
	lines = open(file_name, 'r').readlines()
	lines[line_num] = text
	out = open(file_name, 'w')
	out.writelines(lines)
	out.close()

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
print '\npermissions currently in the .apk file in this directory:\n'

permission = readPermissions()
for value in permission:
	print str(value) + str(permission[value])

removePermission = raw_input('permissions to remove (sparated by commas, e.g. "1,5,12"):')
print ('removing '+str(removePermission))
removePermission = removePermission.split(',')

for lineNumber in removePermission:
	print(type(lineNumber))
	replace_line('./TestApp/AndroidManifest.xml',int(lineNumber),'')
