# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 23:39:33 2020

@author: Devanshu
"""

import sys
import zipfile, os

def backup(folder):
	print("Checking folder...")
	folder = os.path.abspath(folder)
	offset=1
	while True:
		zip_name=os.path.basename(folder)+'_'+str(offset)+'.zip'
		if os.path.exists(zip_name):
			break
		print("Starting Backup...")
		#offset+=1
		print("Successfully created file ",zip_name)
		backupzip=zipfile.ZipFile(zip_name,'w')
		for foldername,subfolders,filenames in os.walk(folder):
			backupzip.write(foldername)
		backupzip.close()
		print("done")
		
		
print("Arrguments: :",str(sys.argv))
folderName = sys.argv[1]
backup(folderName)