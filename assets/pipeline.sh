#!/usr/bin/env bash

if [ $(python3 commentTest.py) == 1 ]; then
	echo "There are missing or incorrectly formatted comments!"
	exit	

fi

echo "Files are correctly commented."

if [ $(python3 renderingTest.py) == ??? ]; then
	echo "There is problem(s) in rendering the image assets."
	exit
	
fi

npm install
npm run build
