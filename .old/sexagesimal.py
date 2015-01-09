#!/usr/bin/python

import math
import Image
from random import randint

def main():
        # Open and read the file
        f = open("sexag.txt", 'r')
        orig = ""
        for line in f:
                orig += line

        # Get each word of the text
        content = orig.split() 

        # Collect data into different forms: characters, hexidecimal, integers
        intArray = []
        hexString = ""
        charString = ""

        for s in content:
                # Cast to int and hex
                sInt = sexToInt(s)
                sHex = intToHexStr(sInt)
                
                # Add to data already casted
                intArray.append(sInt)
                hexString += sHex
                charString += chr(ord('A') + sInt%26)
	
	#printDict(listFrequency(intArray))
	
        
        #sepInts = seperateList(intArray, 16)
        
        # Numbers: (10, 7), (10, 3), (50, 5), 1
        mani = []
        numbers = [17, 13, 55, 1]
	for i in range(len(intArray)):
		mani.append((intArray[i] + (numbers[i%len(numbers)]))%26)
       	
       	
       	time = timeData()
       	new = []
       	for i in range(len(intArray)):
        	new.append(time[i] ^ intArray[i])
        
        
        matchCount = 0
        for i in range((len(new)/2)):
        	if(new[i] == new[i+len(new)/2]):
        		matchCount += 1
        	else:
        		matchCount += -1
        	print str(new[i]) + " - " + str(new[i+len(new)/2])
        	#print new[i] - new[i+len(new)/2]
        
        newAsc = ""
        for i in new:
		newAsc += chr(ord('A') + i%26)
		
	for group in seperateList(new, 8):
		print group
	print newAsc
        
        castToImage(new)

def timeData():
	f = open("time.txt", 'r')
	txt = ""
	for line in f:
		txt += line
	
	data = []
	for i in range(len(txt)/2):
		cur = txt[i] + txt[len(txt)-i-1]
		data.append(int(cur, 16))
	return data
	

# Converts the original data into an int
def sexToInt(s):
        ret = (int(s[0])) * 60 # First int is worth 60

        if('0' <= s[1] and s[1] <= '9'):
                ret += ord(s[1]) - ord('0') # 0-9 is worth 0-9

        if('A' <= s[1] and s[1] <= 'Z'):
                ret += ord(s[1]) - ord('A') + 10 # A-Z is worth 10-36

        if('a' <= s[1] and s[1] <= 'z'):
                ret += ord(s[1]) - ord('a') + 26 + 10 # a-x is worth 36-60

        return ret

def listFrequency(l):
	count = {}
	
	for c in l:
		if c in count:
                	count[c] = count[c] + 1
               	else:
               		count[c] = 1
        
        return count

def printDict(d):
	for key in d:
		print str(key) + " - " + str(d[key])
		
def printDictGr(d):
	for key in d:
		xs = ""
		for i in range(d[key]):
			xs += "X"
		print str(key) + " " + xs
	
# Change int into nicely formated hex string
def intToHexStr(i):
        hexS = hex(i).upper()
        hexS = hexS[2:] # Remove 0x at beginning of string
        if len(hexS) == 1:
                hexS = "0" + hexS # Makes sure everything is 2 digits

        return hexS

# Separate list l into parts of size n
def seperateList(l, n):
        ret = []

        for i in range(int(math.ceil(len(l)/n))): # Create list with right amount of lists
                ret.append([])

        for i in range(len(l)): # Add items to appropriate list
                ret[int(math.floor(i/n))].append(l[i])
        
        return ret

# Put data into an image (no interesting results)
def castToImage(data):
        sepInts = seperateList(data, 1) # Separate data into groups of 4 (RGBA)
        img = Image.new('RGB', (16,16), "black") # Create a new black image
        pixels = img.load() # Create the pixel map

        for i in range(16): # For every pixel:
                for j in range(16):
                        color = sepInts[(i*16) + j]
                        pixels[i,j] = (color[0], color[0], color[0]) # Set the colour accordingly

        img.save("/home/misha/Dropbox/3301/2014/sexag", "bmp")

def avgWords():
	f = open("text.txt", 'r')
	txt = ""
	for line in f:
		txt += line.upper()
	printDictGr(listFrequency(txt))

main()