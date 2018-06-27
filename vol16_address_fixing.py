from vol16_address_tally import addressdict
import csv

#Enter your filename in quotes here
filetoclean = 'v16_data.csv'
output = 'cleanedaddresses_v16.csv'
of_fields = ['Row','File','Number','Name','Type','Other','City','Updated','Match','D6?']

csvfile = open(filetoclean, 'r')
outfile = open(output,'w')
for field in of_fields:
	outfile.write(field+',')
outfile.write('\n')
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile,fieldnames = of_fields)

streetnamelist = []
f = open('d6_streets.csv','r')
lines = f.readlines()
for line in lines:
	streetnamelist.append(line.split(',')[0])

def fixaddresses(streetname):
	if streetname in ('ARENDEL','ARINDEL'):
		newname = 'ARUNDEL'
	elif streetname in ('ASPLING'):
		newname = 'ASPELING'
	elif streetname in ('ARYE','AYNE'):
		newname = 'AYRE'
	elif streetname in ('BALMORAL'):
		newname = 'BALIMORAL'
	elif streetname in ('BLYTH'):
		newname = 'BLYTHE'
	elif streetname in ('CANNIN','COMMON'):
		newname = 'CANON'
	elif streetname in ('CANTEBURY', 'CANTERBURY','CENTERBURY'):
		newname = 'CANTURBURY'
	elif streetname in ('CHATHAN','CLATHAM'):
		newname = 'CHATHAM'
	elif streetname in ('CHYDE'):
		newname = 'CLYDE'
	elif streetname in ('CALLEGE'):
		newname = 'COLLEGE'
	elif streetname in ('CAMBORNE','COMBRINCK'):
		newname = 'COMBRINK'
	elif streetname in ('DE KORTES','DE RODES','DEKORTE'):
		newname = 'DE KORTE'
	elif streetname in ('DE VIELIER','DE VILLERS','DE VILLIEN','DE VILLIER','DE VILLIES','DEVILLES','DEVILLIERS'):
		newname = 'DE VILLIERS'
	elif streetname in ('DEWAAL','DE WAAL'):
		newname = 'DE WAALS'
	elif streetname in ('EARTH'):
		newname = 'ERITH'
	elif streetname in ('ECKARDT','ECKHARD','ECKHARDT','ELKHARDT'):
		newname = 'ECKARD'
	elif streetname in ('GAY','GREY'):
		newname = 'GRAY'
	elif streetname in ('GOOFFREY'):
		newname = 'GODFREY'
	elif streetname in ('GRAND VIEW','GRANDVIEW','GRANDVIEWS'):
		newname = 'GRAND VUE'
	elif streetname in ('LESER'):
		newname = 'LESAR'
	elif streetname in ('LESS'):
		newname = 'LEE'
	elif streetname in ('LOCK','LOEH'):
		newname = 'LOCH'
	elif streetname in ('MCGREGOR'):
		newname = 'MC GREGOR'
	elif streetname in ('MILAN'):
		newname = 'MILLAN'
	elif streetname in ('MORENT'):
		newname = 'MOUNT'
	elif streetname in ('NEWMARK','NEWMARKET'):
		newname = 'NEW MARKET'
	elif streetname in ('NULTON'):
		newname = 'MILTON'
	elif streetname in ('PARDIN','PARKINS','PARLEIN'):
		newname = 'PARKIN'
	elif streetname in ('PETERSEN'):
		newname = 'PEDERSEN'
	elif streetname in ('BLYMOUTH'):
		newname = 'PLYMOUTH'
	elif streetname in ('PONTIAC'):
		newname = 'PONTAC'
	elif streetname in ('PRINSON'):
		newname = 'PRIMROSE'
	elif streetname in ("QUEEN'S",'QUEENS'):
		newname = 'QUEEN'
	elif streetname in ('RAVEMERAIJ'):
		newname = 'RAVENSCRAIG'
	elif streetname in ('RIEBACK','RIEBECK','RIEBEECK'):
		newname = 'REINBACH'
	elif streetname in ('RUGTER','RUTGEN','RUTGERS'):
		newname = 'RUTGER'
	elif streetname in ('SACKVILLE'):
		newname = 'SACKSVILLE'
	elif streetname in ('SHEPHERD','SHEPPARTD'):
		newname = 'SHEPPARD'
	elif streetname in ('SIRDOWRY'):
		newname = 'SIR LOWRY'
	elif streetname in ("ST PHILIP'S",'ST.PHILLIPS'):
		newname = 'ST PHILLIPS'
	elif streetname in ('ST. VINCENT'):
		newname = 'ST VINCENT'
	elif streetname in ('STERLING'):
		newname = 'STIRLING'
	elif streetname in ('STOVE'):
		newname = 'STONE'
	elif streetname in ('SHULKERIS',"STUCKER'S"):
		newname = 'STUCKERIS'
	elif streetname in ('TENANT'):
		newname = 'TENNANT'
	elif streetname in ('UPPER ASHELY'):
		newname = 'UPPER ASHLEY'
	elif streetname in ('UPPER CANTEBURY','UPPER CANTERBURY'):
		newname = 'UPPER CANTURBURY'
	elif streetname in ('VAN DER LEUR','VANDELAUS'):
		newname = 'VAN DE LEUR'
	elif streetname in ('VIRGINA'):
		newname = 'VIRGINIA'
	elif streetname in ('VOGELGESANT','VOGELGEZANG'):
		newname = 'VOGELZANG'
	elif streetname in ('WISHT'):
		newname = 'WICHT'
	elif streetname in ('WILLIAMS'):
		newname = 'WILLIAM'
	elif streetname in ('WINDSER'):
		newname = 'WINDSOR'
	elif streetname in ('YREDE'):
		newname = 'VREDE'
	else:
		newname = streetname
	return newname

autoinc = 0

for row in reader:
	autoinc += 1
	rowid = row['Filename']+ "-" + row['Row']
	number = row['Number'].strip()
	update = ''
	match = ''
	name = row['Street Name'].upper().strip()
	newname = fixaddresses(name)
	if newname != name:
		update = True
	if newname in streetnamelist:
		match = True
	stype = row['Type '].strip().upper()
	other = row['Other'].strip().upper()
	city = row['City'].strip().upper()
	d6 = row['D6 (Y/N/M)'].strip()
	if d6 == '':
		if city not in ('CAPE TOWN','CT','C.T.',''):
			d6 = 'N'
	row = {
		'Row': autoinc,
		'File': rowid,
		'Number': number,
		'Name': newname,
		'Type': stype,
		'Other': other,
		'City': city,
		'Updated': update,
		'Match': match,
		'D6?': d6
	}
	writer.writerow(row)

f.close()
csvfile.close()
outfile.close()