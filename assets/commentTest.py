import glob

headerComment = "/* Name: Kyle Beaumont, ID: 1505627 */\n"
returnFlag = 0

for fileName in glob.glob('src/*.ts'):
	file = open(fileName)
	line = file.readline()
	if line != headerComment:
		print(file.name + " doesn't contain the correct comment format.")
		returnFlag = 1;
	
file.close()

for fileName in glob.glob('src/*.tsx'):
	file = open(fileName)
	line = file.readline()
	if line != headerComment:
		print(file.name + " doesn't contain the correct comment format.")
		returnFlag = 1;
	
file.close()

return returnFlag
