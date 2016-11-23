# Author: Jake Lawrence
# Date: Sunday, November 21, 14:02:37
# Description: Reads two files and determines if they are equal. A percentage fo equivalence is also printed to
#			   the console, along with the differences, giving it a github sort of feel. The percentage 
#              functionality only works for text based files

# although it shows that I am using PIL, and technically I am,
# I am actually using Pillow which is a fork of PIL because
# PIL is a dying library.
from PIL import Image
# I am using os because it is pretty much the go to python
# library when using file paths. I could probably get by without
# using os and just use plain attributes of 'name' or 'filename'
# but os works very well with splitext and it save a bt of complexity.
import os

# --------file streams-------- #

# text based files
# text files
textFile1 = open('testFiles/textFile1.txt',  'r')
textFile2 = open('testFiles/textFile2.txt',  'r')
# textFile3 is the same as textFile1 to test equivalent files
textFile3 = open('testFiles/textFile3.txt',  'r')

# binary files
binaryFile1 = open('testFiles/binaryFile1.bin', 'r')
binaryFile2 = open('testFiles/binaryFile2.bin', 'r')
# binaryFile3 is the same as binaryFile1 to test equivalent files
binaryFile3 = open('testFiles/binaryFile3.bin', 'r')

# csv files
csvFile1 = open('testFiles/csvFile1.csv',  'r')
csvFile2 = open('testFiles/csvFile2.csv',  'r')
# csvFile3 is the same as csvFile1 to test equivalent files
csvFile3 = open('testFiles/csvFile3.csv',  'r')

# image based files
# jpeg images
jpegFile1 = Image.open('testFiles/jpegFile1.jpg', 'r')
jpegFile2 = Image.open('testFiles/jpegFile2.jpg', 'r')
# jpegFile3 is the same as csvFile1 to test equivalent files
jpegFile3 = Image.open('testFiles/jpegFile3.jpg', 'r')

# png files
pngFile1 = open('testFiles/pngFile1.png', 'r')
pngFile2 = open('testFiles/pngFile2.png', 'r')
# pngFile3 is the same as csvFile1 to test equivalent files
pngFile3 = open('testFiles/pngFile3.png', 'r')

# ----------------------------- #

# determines which process should be taken to compare files
def compareFiles(file1, file2):
	# this is put in place because jpegs only have a filename attribute but pretty
	# much every file other than jpeg has a name attribute
	try:
		file1_type = os.path.splitext(file1.filename)[1]
		file2_type = os.path.splitext(file2.filename)[1]
		print("File 1: " + os.path.splitext(file1.filename)[0] + " and " + "File 2: " + os.path.splitext(file2.filename)[0] + ":")
	except:
		file1_type = os.path.splitext(file1.name)[1]
		file2_type = os.path.splitext(file2.name)[1]
		print("File 1: " + os.path.splitext(file1.name)[0] + " and " + "File 2: " + os.path.splitext(file2.name)[0] + ":")

	# checks to see if the files are of equivalent types
	# techinically a comparison between types is possible
	# but it just makes more sense to disallow that 
	if(file1_type == file2_type):
		# if the files are images
		if(file1_type == '.jpg' or file1_type == '.png'):
			compareImages(file1,file2)
		# if the files are text based
		# there are more text based files that exist
		# but I just used these to demonstrate functionality
		elif(file1_type == '.txt' or file1_type == '.bin' or file1_type == '.csv'):
			compareTextBased(file1, file2)
		# if something else
		else:
			print("Invalid file type.\n")
	else:
		print("The given files are not the same type of file.\n")

# compares two images
def compareImages(file1, file2):
	# allows png and jpg compatibility
	try:
		file1_path = os.path.splitext(file1.filename)[0] + os.path.splitext(file1.filename)[1];
		file2_path = os.path.splitext(file2.filename)[0] + os.path.splitext(file2.filename)[1];
	except:
		file1_path = os.path.splitext(file1.name)[0] + os.path.splitext(file1.name)[1];
		file2_path = os.path.splitext(file2.name)[0] + os.path.splitext(file2.name)[1];
	file1.close()
	file2.close()
	# loads the files as images
	file1 = Image.open(file1_path, 'r')
	# creates a tuble of the pixel values
	data_f1 = file1.load()
	file2 = Image.open(file2_path, 'r')
	# creates a tuble of the pixel values
	data_f2 = file2.load()
	# if the images aren't the same dimensions
	if(file1.size != file2.size):
		print("The given images are not equal.\n")
		return
	# checks each pixel value against eachother
	for x in range(0, file1.size[0]):
		for y in range(0, file1.size[1]):
			if(data_f1[x,y] != data_f2[x,y]):
				print("The given images are not equal.\n")
				return
	print("The given images are equal.\n")
	file1.close();
	file2.close()

# compare two files
def compareTextBased(file1, file2):
	file1_path = os.path.splitext(file1.name)[0] + os.path.splitext(file1.name)[1];
	file2_path = os.path.splitext(file2.name)[0] + os.path.splitext(file2.name)[1];
	# file that contains the differences
	differencesFile = open('differencesFile.txt', 'w')
	sizeOfFile1 = 0
	sizeOfFile2 = 0
	sizeOfDF = 0

	while True:
		# reads character by character
	    f1c = file1.read(1)
	    f2c = file2.read(1)
	    # if a difference is found
	    if f1c != f2c:
	    	# logs the given difference
	    	differencesFile.write(f2c)
	    	sizeOfDF += 1
	    # end of files
	    if not f1c and not f2c:
	    	break
	    # if a char is found increment the size of the file
	    if f2c:
	    	sizeOfFile2 += 1

	differencesFile.close()

	differencesFile = open('differencesFile.txt', 'r')
	# creates percentage of similarity
	percentageOfDifference = (100*(sizeOfFile2 - sizeOfDF))/sizeOfFile2
	# if not the same
	if(percentageOfDifference < 100):
		print("The files are not the same.")
		print("Differences between File 1 and File 2: " + differencesFile.read())
	print("File 1 is " + str(percentageOfDifference) + " percent equal to File 2\n")
	differencesFile.close()

#closes files that were possibly opened
def closeFiles():
	textFile1.close()
	textFile2.close()
	textFile3.close()
	binaryFile1.close()
	binaryFile2.close()
	binaryFile3.close()
	csvFile1.close()
	csvFile2.close()
	csvFile3.close()

#--------test cases--------#

# fyi: file1 != file2
#	   file1 = file3
# change the file numbers below to test

compareFiles(textFile1,textFile3)

compareFiles(binaryFile1,binaryFile3)

compareFiles(csvFile1,csvFile3)

compareFiles(pngFile1,pngFile3)

compareFiles(jpegFile1,jpegFile3)

#-----------------------#

# closes any files that haven't been closed already
closeFiles()



