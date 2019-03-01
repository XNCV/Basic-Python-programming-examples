import sys
import hashlib
import os

file_out = open("checksums", "w+")
dir_files = os.listdir(sys.argv[1])
list_files = []
for file in dir_files:
	list_files.append(file)
list_files.sort()
for file in list_files:
	string = hashlib.md5(file.encode('utf-8')).hexdigest()
	string = string + ' ' + file + '\n'
	file_out.write(string)
file_out.close()
