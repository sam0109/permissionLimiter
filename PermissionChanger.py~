#!/usr/bin/python
import subprocess
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of the .apk file (excluding .apk)")
args = parser.parse_args()

def readPermissions():
	permission = {}
	subprocess.call("apktool d -f ./"+args.filename+".apk", shell=True)
	manifest = open( "./"+args.filename+"/AndroidManifest.xml")
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

lines = open('./'+args.filename+'/AndroidManifest.xml', 'r').readlines()
for lineNumber in removePermission:
	lines[int(lineNumber)] = ''

out = open('./'+args.filename+'/AndroidManifest.xml', 'w')
out.writelines(lines)
out.close()

subprocess.call("apktool b -f ./"+args.filename+"/", shell=True)
