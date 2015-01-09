#!/usr/bin/python

# Possible keys:
# Runes outguess
# Xor combinations of all of above
# 3301/1103 */^/xor
# Pi

import dparse
import fractions

primes = []
fibs = []
totients = []

time1 = dparse.hexToInt(dparse.txtToHex(dparse.readFile("time1.hex")))
time2 = dparse.hexToInt(dparse.txtToHex(dparse.readFile("time2.hex")))
time3 = dparse.hexToInt(dparse.txtToHex(dparse.readFile("time3.hex")))
sexag = dparse.sexToInt(dparse.txtToSex(dparse.readFile("sexag.sex")))
cune1 = [17,15,55,1]
cune2 = [17,15,50,5,1]
cune3 = [10,7,10,5,50,5,1]

def initPrimes(m):
        for i in range(2,m):
                isPrime = True
                for j in range(2,i/2+1):
                        if i%j == 0:
                                isPrime = False
                                break
                if isPrime:
                        primes.append(i)

def initFibs(m):
        f1 = 1
        f2 = 1

        fibs.extend([1,1])
        
        while len(fibs) <= m:
                temp = f2
                f2 = f1 + f2
                f1 = temp
                fibs.append(f2)

def initTotients(m):
        for i in range(1,m):
                count = 0
                for j in range(1,i+1):
                        if fractions.gcd(i, j) == 1:
                                count += 1
                totients.append(count)

initPrimes(2000)
initFibs(500)
initTotients(500)

allKeys = [range(500), primes, fibs, totients, time1, time2, time3, sexag]
