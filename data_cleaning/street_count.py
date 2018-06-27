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
	if len(street_list) == 0:
		pass
	elif len(street_list) == 2:
		ref_list.append(street_list[0].strip().upper())
	else:
		street = ''
		street_list = street_list[:-1]
		for item in street_list:
			street += (item + ' ')
		ref_list.append(street.strip().upper())

ref_file.close()

csvfile = open(filetoclean, 'r')
reader = csv.DictReader(csvfile)
outfile = open(output,'w')
outfile.write('StreetName,Count,Match\n')
fields = ['StreetName','Count','Match']
writer = csv.DictWriter(outfile,fieldnames = fields)

addressdict = {}
for row in reader:
	street = row['Street Name'].strip().upper()
	if street not in addressdict:
		addressdict[street] = 0
	addressdict[street] += 1

csvfile.close()

for item in sorted(addressdict.keys()):
	if item != '':
		street = item
		count = addressdict[item]
		match = (item in ref_list)
		row = {'StreetName': street, 'Count': count, 'Match': match}
		writer.writerow(row)

outfile.close()