import csv

f = open('reformatted_vol_16_data.csv','r')
outfile = open('v16_cleaned_for_plotting.csv','w')
outfile.write('Address,Input,Filename,Vol,Page,Row,Date,Seq,Surname,Given Name,Father,Mother,Date of Birth,Number,Street Name,Type,City,Other,Profession,Surname 1,Given Name 1,Surname 2,Given Name 2,Surname 3,Given Name 3,Who Baptized,Additional Archival Information\n')
headers_list = ['Address','Input','Filename','Vol','Page','Row','Date','Seq','Surname','Given Name','Father','Mother','Date of Birth','Number','Street Name','Type','City','Other','Profession','Surname 1','Given Name 1','Surname 2','Given Name 2','Surname 3','Given Name 3','Who Baptized','Additional Archival Information']
reader = csv.DictReader(f)
writer = csv.DictWriter(outfile, fieldnames = headers_list)

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
	elif streetname in ('HORSBERG','HORSBERGH','HOSBURGH'):
		newname = 'HORSBURG'
	elif streetname in ('LAVENDER HILL'):
		newname = 'LAVENDER'
	elif streetname in ('LESER','LEVER'):
		newname = 'LESAR'
	elif streetname in ('LESS'):
		newname = 'LEE'
	elif streetname in ('LOCK','LOEH'):
		newname = 'LOCH'
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
	elif streetname in ('ROSE'):
		newname = 'ROOS'
	elif streetname in ('SACKVILLE'):
		newname = 'SACKSVILLE'
	elif streetname in ('SHEPHERD','SHEPPARTD'):
		newname = 'SHEPPARD'
	elif streetname in ('SELTARK'):
		newname = 'SELKIRK'
	elif streetname in ('SIRDOWRY'):
		newname = 'SIR LOWRY'
	elif streetname in ('SYDNEY'):
		newname = 'SIDNEY'
	elif streetname in ('SPRINGFELD','SPRINGFIELD TERRACE OFF PONTIAC'):
		newname = 'SPRINGFIELD'
	elif streetname in ('SORREY'):
		newname = 'SOREY'
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

for row in reader:
	street = row['Street Name'].strip().upper()
	newname = fixaddresses(street)
	address = ""
	if str(row['Number']).strip()[-1] not in ['1','2','3','4','5','6','7','8','9','0']:
		address += str(row['Number']).strip()[:-1]
	else:
		address += str(row['Number']).strip()
	address += " {}".format(newname)
	if newname in ['FAWLEY','VERNON','SELWYN']:
		streettype = 'TERRACE'
	elif newname in ['LAVENDER','SUMMER']:
		streettype = 'HILL'
	else:
		streettype = row['Type'].upper().strip()
	row = {
		'Address': address,
		'Input': row['Input'],
		'Filename': row['Filename'],
		'Vol': row['Vol'],
		'Page': row['Page'],
		'Row': row['Row'],
		'Date': row['Date'],
		'Seq': row['Seq'],
		'Surname': row['Surname'],
		'Given Name': row['Given Name'],
		'Father': row['Father'],
		'Mother': row['Mother'],
		'Date of Birth': row['Date of Birth'],
		'Number': row['Number'].strip(),
		'Street Name': newname,
		'Type': streettype,
		'City': row['City'].strip().upper(),
		'Other':row['Other'].strip().upper(),
		'Profession': row['Profession'],
		'Surname 1': row['Surname 1'],
		'Given Name 1': row['Given Name 1'],
		'Surname 2': row['Surname 2'],
		'Given Name 2': row['Given Name 2'],
		'Surname 3': row['Surname 3'],
		'Given Name 3': row['Given Name 3'],
		'Who Baptized': row['Who Baptized'],
		'Additional Archival Information': row['Additional Archival Information']
		}
	writer.writerow(row)

outfile.close()
f.close()