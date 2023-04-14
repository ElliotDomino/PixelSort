from PIL import Image
from random import random
import numpy as np

def quickSort(data,first,last):
	if first < last:
		pivot = partition(data, first, last)
		quickSort(data, first, pivot - 1)
		quickSort(data, pivot + 1, last)

def partition(data, first, last):
	pivotValue = data[first]
	leftMark = first + 1
	rightMark = last
	done = False

	while not done:

		while leftMark <= rightMark and data[leftMark] <= pivotValue:
			leftMark = leftMark + 1

		while rightMark >= leftMark and data[rightMark] >= pivotValue:
			rightMark = rightMark - 1

		if rightMark < leftMark:
			done = True

		else:
			temp = data[leftMark]
			data[leftMark] = data[rightMark]
			data[rightMark] = temp

	temp = data[first]
	data[first] = data[rightMark]
	data[rightMark] = temp
	return rightMark

def fileToArray(filename):
	# Open the image file
	image = Image.open(filename)

	# Get the pixel values as a 2D array
	pixels = list(image.getdata())
	width, height = image.size
	pixels = [pixels[i:i+width] for i in range(0, len(pixels), width)]

	# return the pixel values
	return pixels

def arrayToFile(pixels, filename):
	# Convert the pixel values to a flattened list
	width, height = len(pixels[0]), len(pixels)

	flatPixels = []
	for row in pixels:
	    for pixel in row:
	        flatPixels.append(pixel)

	# Create an image object and save it
	image = Image.new("RGB", (width, height))
	image.putdata(flatPixels)
	image.save(filename)
	return image

def getAverageVibranceFromArray(pixels):
	# Compute the standard deviation of the pixel values in each row.
	vibrance = np.std(pixels, axis=1)

	averages = []
	for item in vibrance:
		averages.append(np.average(item))

	# Compute the average vibrance for all rows.
	minVibrance = min(averages)
	avgVibrance = np.mean(averages)
	maxVibrance = max(averages)

	return avgVibrance, minVibrance, maxVibrance

def sortSelection(pixelArray):
	
	height = len(pixelArray)
	width = len(pixelArray[0])

	print(f"{height=} (max {height - 1}), {width=} (max {width - 1})")

	yUp = height - int(input("Y Lower bound: "))
	yLow = height - int(input("Y Upper bound: "))

	xLow = int(input("X Lower bound: "))
	xUp = int(input("X Upper bound: "))

	# sort a selection (rectangle)
	for y in range(yLow, yUp+1):
		quickSort(pixelArray[y], xLow, xUp)

def main():
	fileInName = input("Filename of input: ")

	running = True
	compound = False

	pixelArray = fileToArray(fileInName)

	while running:
		# percentSort = float(input("Percent Chance to sort each row? "))

		sortSelection(pixelArray)

		if not compound:
			filePrefix = fileInName.split(".")[0]
			fileSuffix = fileInName.split(".")[1]
			name = f"{filePrefix}-PROCESSED.{fileSuffix}"

		arrayToFile(pixelArray, name)

		command = input("Q to quit, Enter to continue (Layer effect)").lower()
		if command == "q":
			running = False
		else:
			compound = True

	print("Bye!")
		

if __name__ == "__main__":
	main()