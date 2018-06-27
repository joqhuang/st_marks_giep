import os
import csv

old_directory = open('SAFR0017D_DN001_Directory.txt','r')
directory_lines = old_directory.readlines()
old_directory.close()
old_directory_list = []
for line in directory_lines:
	line = line.strip()
	if line[0] == 'S' and len(line) > 20:
		old_directory_list.append(line)

volume_overview = 'record_volumes_overview.csv'
csvfile = open(volume_overview,'w')
csvfile.write('Volume,Dates,Filesize,Total Files,Record Pages,Old Directory Name(s)\n')
csv_headers = ['Volume','Dates', 'Filesize', 'Total Files','Record Pages','Old Directory Name(s)']
writer = csv.DictWriter(csvfile,fieldnames = csv_headers)

path =  os.getcwd()
directories = os.listdir(path)

for directory in directories:
	volume = directory.split('_')[0]
	date = directory.split('_')[-1]
	size = ''
	files = 0
	pages = 0
	filenames = os.listdir(directory)
	for file in filenames:
		files += 1
		if file[-1] == 'f':
			try:
				int(file[5])
				pages += 1
			except:
				print("{} is a calibration page and not being counted".format(file))
	old_dir = []
	for item in old_directory_list:
		if item.lower().split('-')[-2] == directory.split('_')[-1].split('-')[0]:
			old_dir.append(item)
	row = {'Volume': volume,
			'Dates': date, 
			'Filesize': size, 
			'Total Files': files,
			'Record Pages': pages,
			'Old Directory Name(s)': str(old_dir)
			}
	writer.writerow(row)

csvfile.close()
