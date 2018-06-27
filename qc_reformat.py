import os
import csv

path =  os.getcwd()
filenames = os.listdir(path)

outname = 'ImageQC.csv'
outfile = open(outname,'w')
qcfields = ['Date','Auditor','Filename','Passed']
outfile.write('Date,Auditor,Filename,Passed\n')
writer = csv.DictWriter(outfile,fieldnames = qcfields)

for name in filenames:
	if name[:4] == "Eval":
		f = open(name,'r')
		lines = f.readlines()
		name = lines[1].split('=')[-1].strip()
		date = lines[3].split('=')[-1].split()[0]
		for idx in range(len(lines)):
			if lines[idx][:2] == "[I":
				fname = lines[idx+1].split('=')[-1].split('{')[-1].strip()
				row = {'Date':date,'Auditor':name,'Filename':fname,'Passed':'Y'}
				writer.writerow(row)