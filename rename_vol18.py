import os

path =  os.getcwd()
filenames = os.listdir(path)

for filename in filenames:
	if filename[-3:] == "tif":
	    os.rename(filename, "vol18_"+filename[59:])