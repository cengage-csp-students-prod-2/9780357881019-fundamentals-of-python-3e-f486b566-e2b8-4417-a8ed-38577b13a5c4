"""
Author: Ashley Francis
Date written: 02/11/2025
Assignment: Module 04 Practice Exercise 5-8
This programs is designed to output the unique words and
their frequencies in alphabetical order.
"""

inName = input("Enter the input file name: ")

inputFile = open(inName, 'r')
uniqueWords = {}

for line in inputFile:
    words = line.split()

    for word in words:
        if word in uniqueWords:
            uniqueWords[word] = uniqueWords[word] + 1
        else:
            uniqueWords[word] = 1

inputFile.close()

wordList = list(uniqueWords.keys())
wordList.sort()

for word in wordList:
    print(word, uniqueWords[word])# Write your program here
