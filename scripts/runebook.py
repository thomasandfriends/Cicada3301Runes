#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string

import dparse
import dstats
import dmanip
import gemprim
import simple_crypto

raw = dparse.readFile("runes.rune")

rawPages = raw.split("\n\n")

# List of pages
pages = []
for page in rawPages:
        curPage = []
        for word in page.split("•"):
                primeWord = []
                for letter in dmanip.sepStr(word, 3):
                        primeWord.append(gemprim.runeToPrime([letter])[0])
                curPage.append(primeWord)
        pages.append(curPage)

# List of words
words = []
for page in pages:
        words.extend(page)

# List of runes
runes = []
for word in words:
        runes.extend(word)

# Words as strings
strWords = [gemprim.ascToStr(gemprim.primeToAsc(word)) for word in words]

# Lengths of words
wordLengths = [len(word) for word in words]

# Translate all into block of text
txt = ""
for page in pages:
        for word in page:
                for letter in word:
                        letter = gemprim.primeToAsc([letter])[0]
                        for c in letter:
                                if c == "/":
                                        continue
                                if 'A' <= c <= 'Z':
                                        txt += c
                txt += " "
        txt += "\n\n"

hashPage = pages[55]

dstats.graphFreq([gemprim.ascToStr(gemprim.primeToAsc(word)) for word in hashPage], 1)

sys.exit()

hashPage = [gemprim.primeToInt(i) for i in hashPage]
plainPage = []

count = 0
for word in hashPage:
        plainWord = []
        for c in word:
                plainWord.append((c - primes[count] + 1) % 29)
                count += 1

        plainPage.append(plainWord)

print [gemprim.primeToRune(gemprim.intToPrime(word)) for word in hashPage]
print [gemprim.ascToStr(gemprim.primeToAsc(gemprim.intToPrime(word))) for word in plainPage]


# Get freq of every page
# for ip in range(len(pages)):
#         print "Page " + str(ip) + ":"
#         page = pages[ip]
#         runes = []
#         for word in page:
#                 runes.extend([gemprim.primeToAsc([c])[0] for c in word])
#         dstats.graphFreq(runes)
#         raw_input("...")

### Results:
### Every page has variation in frequencies
### Which letters appear more doesn't seem to have a pattern - should double check though

# Possible keys:
# 256B x3
# 256B sexagesimal
# Runes outguess
# 17,13,55,1
# Xor combinations of all of above
# Sequences of primes, fibs, totients

# Possible applications:
# Xor
# +, -, *
# 3301-n (and variations)

# Numbers from runes:
# Primes
# Index
# From IRC: Sets of aetts??
# Combinations

# Applied to:
# Pages
# Whole book
