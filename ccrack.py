import sys 
import argparse 
import numpy

def analyze(cipher):
    #cipher = "Wudyki myjxekj utksqjyed yi byau iybluh yd jxu cydu."
    max = 0

    rfd = len(cipher)

    # English Letter Frequency Counts: http://norvig.com/mayzner.html
    weight = [8.04, 1.48, 3.34, 3.82, 12.49, 2.40, 1.87, 5.05, 7.57, 0.16, 0.54, 4.07, 2.51,
    7.23, 7.64, 2.14, 0.12, 6.28,  6.51, 9.28, 2.73, 1.05, 1.68, 0.23, 1.66, 0.09]

    freq = numpy.array([0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0])
    
    s = [0, 0, 0, 0, 0,
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

    freq = freq/rfd
    
    # https://www.xarg.org/2010/05/cracking-a-caesar-cipher/
    for off in range(0, 26):
        for i in range(0, 26):
            wi = (i + off) % 26
            s[off] +=  freq[i] * weight[wi]
            if (max < s[off]):
                max = s[off]

    key = (26 - s.index(max)) % 26
    print(key)

def main():
    parser = argparse.ArgumentParser(description='Attempts to guess the key of a caesar cipher. \
        Returns the mostly likely key using found using frequency analysis of the characters in the message.')
    parser.add_argument('cipher', help='The caesar cipher message to perform cryptanalsis on.')
    args = parser.parse_args()
    analyze(args.cipher)

main()