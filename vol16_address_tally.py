import csv

#Enter your filename in quotes here
filetoclean = 'data.csv'
output = 'street_inventory.csv'
reference = 'reference.csv'

ref_file = open(reference,'r')
ref_reader = csv.DictReader(ref_file)

ref_list = []
for row in ref_reader:
	street_list = row['STREETNAME'].split()
	if len(street_list) < 1:
		pass
	elif len(street_list) < 3:
		ref_list.append(street_list[0].strip().upper())
	else:
		street = ''
		for item in street_list:
			street += (item + ' ')
		ref_list.append(street.strip().upper())

ref_file.close()

csvfile = open(filetoclean, 'r')
reader = csv.DictReader(csvfile)
oufile = open(output,'w')
oufile.write('StreetName,Count,Match\n')
fields = ['StreetName','Count','Match']
writer = csv.DictWriter(outfile,fieldnames = fields)

addressdict = {}
for row in reader:
	street = row['Street Name'].strip()
	if street not in addressdict:
		addressdict[street] = 0
	addressdict[street] += 1

csvfile.close()

for item in addressdict:
	street = item
	count = addressdict[item]
	match = (item in ref_list)
	row = {'StreetName': street, 'Count': count, 'Match': match}
	writer.writerow(row)

outfile.close()