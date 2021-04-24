from os import listdir
from os.path import isfile, join
#mypath is to spacify on local 
mypath = 'D:\AZ-104'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file in onlyfiles:
	print(file)