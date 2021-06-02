import glob

returnFlag = 0

for fileName in glob.glob('src/modules/*/*.tsx'):
	from fileName import render
	try:
        
        componentDidMount()
        
    except:
        returnFlag = 1
        
return returnFlag