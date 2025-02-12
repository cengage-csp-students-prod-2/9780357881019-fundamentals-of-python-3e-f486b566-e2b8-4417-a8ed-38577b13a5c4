"""
Author: Ashley Francis
Date written: 02/11/2025
Assignment: Module 04 Practice Exercise 5-7
This program is designed to print unique words in a file in alphabetical order
"""

def GetUserInput(prompt):
    return input(prompt)

def CreateEmptyList():
    return []

def OpenFile(file_name, mode):
    return open(file_name, mode)

def SplitLineIntoWords(line):
    return line.split()

inName = GetUserInput("Enter the input file name: ")
uniqueWords = CreateEmptyList()

inputFile = OpenFile(inName, 'r')

for line in inputFile:
    words = SplitLineIntoWords(line)
    for word in words:
        if word not in uniqueWords:
            uniqueWords.append(word)

uniqueWords.sort()

for word in uniqueWords:
    print(word)

inputFile.close()
