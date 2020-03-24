#Imports
from zipfile import ZipFile
with ZipFile('bios.zip','w') as zip: 
        # writing each file one by one 
	with open('bios.csv', 'r') as outfile:
		zip.write(outfile)