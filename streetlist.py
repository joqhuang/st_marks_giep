import csv

csvfile = open('cleaned_addresses.csv','r')
reader = csv.DictReader(csvfile)

street_list = []
for row in reader:
	street = row['StrName']
	if street not in street_list:
		street_list.append(street)

outfile = open('d6_streets_updated.csv','w')
outfile.write('StrName\n')
for street in sorted(street_list):
	outfile.write('{}\n'.format(street))
