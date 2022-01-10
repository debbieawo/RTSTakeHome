#!/usr/bin/python
# Author: Debbie Antoine 
# License: Public Domain
# Purpose: Take a path to a text file as an argument
# add hello world to a new line at the beginning of the file
# add goodbye at the end of a new line
import os
import sys

path = "file.txt"
fileName = "newFile.txt"
#Take a path to a text file as an argument
if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)
    fileName = os.path.join(path, fileName)
    open(fileName)

#Add "Hello World" to a new line at the beginning of the file
with open(fileName, "w+") as originalFT: 
    data = originalFT.read()
with open(fileName, "w+") as fileText: 
    fileText.write("Hello World\n"+ data)

#Add "Goodbye" to a new line at the end of the file
    fileText.seek(0,1)
    fileText.write("Goodbye")
    fileText.seek(0)

#with open(fileText) as file:
    print(fileText.read())
    fileText.close()
   