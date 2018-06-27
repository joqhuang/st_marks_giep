import csv

#Enter your filename in quotes here
filetoclean = 'reformatted_vol_16_data.csv'
output = 'street_inventory.csv'
reference = 'd6_streets_updated.csv'

ref_file = open(reference,'r')

ref_list = []
for line in ref_file.readlines():
	ref_list.append(line[:-1])

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