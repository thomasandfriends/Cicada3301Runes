#!/usr/bin/python

def printGrid(numbers):
        for col in numbers:
                print col

def isPrime(n):
        for i in range(2, n/2+1):
                if n%i == 0:
                        return False
        return True    

def getPrimeOrder(n):
        count = 0
        for i in range(2,10000):
                if(isPrime(i)):
                        if(i == n):
                                return count
                        count += 1


numbers = [\
[3258, 3222, 3152, 3038],
[3278, 3299, 3298, 2838],\
[3288, 3294, 3296, 2472],\
[-4516,-1206, 708, 1820]]

for x in range(len(numbers)):
        for y in range(len(numbers[x])):
                numbers[x][y] = 3301 - numbers[x][y]

printGrid(numbers)

print "---"

for x in range(len(numbers)):
        for y in range(len(numbers[x])):
                numbers[x][y] = getPrimeOrder(numbers[x][y])

printGrid(numbers)
