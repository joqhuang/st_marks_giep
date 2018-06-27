import os

path =  os.getcwd()
directories = os.listdir(path)

for direc in directories:
	if direc[0] != '.'  and direc[-2:] != 'py':
		volume = direc.split('_')[0]+"_"+direc.split('_')[1]+"_"
		filenames = os.listdir(direc)

		newfile = open(direc + "/" + volume + 'preservation_metadata.csv','w')
		newfile.write('"NewFilename","FileName","Date","Time","Gain","Exposure","Black","Filter","FStop","Lens","FocalLen","Project","Item","Station","X","Y","UniqueColors","RGBCalibration","Operator Name","Operator ID","Camera Serial No","Repository","Record Locality","Event Type","Dates Covered","Free Comment","BlankPage","Retake","AutoJPEG","AutoGrayscale"\n')		

		dest = direc +"/" +volume+'original_preservation_metadata_files'
		os.mkdir(dest)

		for filename in filenames:
			if filename[-3:] == 'log' and filename[:3] == 'SAF':
				csvfile = open(direc + "/" + filename,'r')
				lines = csvfile.readlines()
				for line in lines[1:]:
					newfile.write(volume+line.split(",")[0][-8:-1]+",")
					newfile.write(line)
			if filename[-3:] == "tif":
				if filename[-12:] == '00000-aa.tif':
					newname = volume+'grayscale.tif'
				elif filename[-12:] == '00000-ab.tif':
					newname = volume+'lsi.tif'
				elif filename[-9:] == '00000.tif':
					newname = volume+'whiteboard.tif'
				elif filename[-12:] == '00001-aa.tif':
					newname = volume+'001.tif'
				elif filename[-9:] == '00001.tif':
					newname = volume+'exterior.tif'
				elif filename[-7:] == '-aa.tif':
					newname = volume+filename[-10:-7]+'-insert.tif'
				else:
				    newname = volume+filename[-7:]
				os.rename(direc +"/" + filename,direc +"/" +newname)
		newfile.close()

		filenames = os.listdir(direc)
		for filename in filenames:
			if filename[-3:] == 'tif':
				try:
					int(filename[-5])
				except:
					if filename[-10:] == 'insert.tif':
						pass
					else:
						os.rename(direc + "/" + filename, dest + "/" + filename)
			else:
				try:
					os.rename(direc +"/" +filename, dest + "/" +filename)
				except:
					pass