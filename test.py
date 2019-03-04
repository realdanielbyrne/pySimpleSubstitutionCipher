import sys 
import argparse
import numpy

cipher = "Wudyki myjxekj utksqjyed yi byau iybluh yd jxu cydu."


rfd = len(cipher)

# English Letter Frequency Counts: http://norvig.com/mayzner.html
weight = numpy.array([8.04, 1.48, 3.34, 3.82, 12.49, 2.40, 1.87, 5.05, 7.57, 0.16, 0.54, 4.07, 2.51,
7.23, 7.64, 2.14, 0.12, 6.28,  6.51, 9.28, 2.73, 1.05, 1.68, 0.23, 1.66, 0.09])

freq = numpy.array([0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0])

s =  [0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0]

for letter in cipher:
    # transform to lowercase, shift to 0:26
    letterIndex = (ord(letter) | 32) - 97
    
    # if one of 26 letters, increment its count
    if (letterIndex >=0  and letterIndex < 26):
        freq[letterIndex] += 1

for off in range(0, 26):
    s[off] += 


#key = (26 - s.index(max(s))) % 26
#print(key)