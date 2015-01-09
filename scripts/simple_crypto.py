#!/usr/bin/python
import sys

def fileToString(f):
	f.seek(0)
	ret = ""	

	for line in f:
		ret += line
	
	return ret

def caesarWithShift(txt, i):
	txt.seek(0)
	for c in txt:
		if ord(c) >= ord('A') and ord(c) <= ord('Z'):
			ret += shiftChar(c, i)
			continue
		ret += c
	ret += '\n'
	return ret

def shiftChar(c, i):
	return (chr(((ord(c)-ord('A')+i)%26)+ord('A')))

def countCharsInFile(txt):
	count = {}
	for c in txt:
		if ord(c) >= ord('A') and ord(c) <= ord('Z'):
			if c in count:
				count[c] = count[c] + 1
			else:
				count[c] = 1
	return count

def countSinglesInFile(txt):
	count = {}
	for word in txt.split():
		if len(word) == 1:
			c = word
			if ord(c) >= ord('A') and ord(c) <= ord('Z'):
				if c in count:
					count[c] = count[c] + 1
				else:
					count[c] = 1
	return count

def removePunc(txt):
	ret = ""
	
	for c in txt:	 
		if ord(c) >= ord('A') and ord(c) <= ord('Z'):
			ret += c

	return ret


def replaceWithDict(txt, d):
	ret = ""
	for c in txt:
		if ord(c) >= ord('A') and ord(c) <= ord('Z') and c in d:
			ret += d[c]			
			continue
		ret += c
	return ret

def countDoubles(txt):
	count = {}
	
	txt = removePunc(txt)
	
	for i in range(len(txt)-1):
		if txt[i] == txt[i+1]:
			if txt[i] in count:
				count[txt[i]] = count[txt[i]] + 1
			else:
				count[txt[i]] = 1
	
	return count

def caesarShiftShift(txt):
	for i in range(26):
		shifted = ""
		print "Shift: " + str(i)
		for c in txt:
			if c >= 'A' and c <= 'Z':
				shifted += shiftChar(c, i)
				i += 1
		
		print shifted
		raw_input("")


	
def printDict(d):		
	for key in d:
		print key + " - " + str(d[key])

def printDictDiffs(d, base1, base2):
	for key in d:
		print "(" + key + ", " + d[key] + ")" + " - " + "(" + str(ord(key)-base1) + ", " + str(ord(d[key])-base2) + ")" 

def main():
	numCount = {}
	
	txt = fileToString(open("/home/misha/Dropbox/cipherchallenge/2b.txt", 'r'))	

	numCount = countCharsInFile(txt)
	printDict(numCount)

	dic = {
	'M':'e',
	#'C':'t',
	}
	
	printDictDiffs(dic, ord('A'), ord('a'))
	
	print replaceWithDict(txt, dic)

	caesarShiftShift(txt)

#main()
