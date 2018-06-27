import csv

#Enter your filename in quotes here
filetoclean = 'Locator2.csv'
output = 'cleaned_addresses.csv'

csvfile = open(filetoclean, 'r')
reader = csv.DictReader(csvfile)
outfile = open(output,'w')
outfile.write('OBJECTID,Id,StrNo,StrName,StrType,Unresolved,Address\n')
fields = ['OBJECTID','Id','StrNo','StrName','StrType','Unresolved','Address']
writer = csv.DictWriter(outfile,fieldnames = fields)

def fixname(name):
	if name == "BALMORAL":
		newname = 'BALIMORAL'
	elif name == 'CONSTITUION':
		newname = 'CONSTITUTION'
	elif name == 'FAWLEY TERRACE':
		newname = 'FAWLEY'
	elif name == 'HORSTLE':
		newname = 'HORSTLEY'
	elif name == 'LAVENDER HILL':
		newname = 'LAVENDER'
	elif name == 'MUIR STREET':
		newname = 'MUIR'
	elif name in ['PANTOC','PONTAC STREET']:
		newname = 'PONTAC'
	elif name == 'REFORM STREET':
		newname = 'REFORM'
	elif name == 'SACKVILLE':
		newname = 'SACKSVILLE'
	elif name == 'ST PHILIPS':
		newname = 'ST PHILLIPS'
	elif name == 'STORE':
		newname = 'STONE'
	elif name == 'SUMMER HILL':
		newname = 'SUMMER'
	elif name == 'SYDNEY':
		newname = 'SIDNEY'
	elif name == 'VAN DELEUR':
		newname = 'VAN DE LEUR'
	elif name == 'VERNON TERRACE':
		newname = 'VERNON'
	else:
		newname = name
	return newname

for row in reader:
	name = row['StrName'].upper().strip()
	newname = fixname(name)
	if newname in ['FAWLEY','VERNON','SELWYN']:
		streettype = 'TERRACE'
	elif newname in ['LAVENDER','SUMMER']:
		streettype = 'HILL'
	else:
		streettype = row['StrType'].upper().strip()
	row = {
		'OBJECTID': row['OBJECTID'],
		'Id': row['Id'],
		'StrNo': row['StrNo'],
		'StrName': newname,
		'StrType': streettype,
		'Unresolved': row['Unresolved'].upper().strip(),
		'Address':"{} {}".format(row['StrNo'],newname)
		}
	writer.writerow(row)

csvfile.close()
outfile.close()