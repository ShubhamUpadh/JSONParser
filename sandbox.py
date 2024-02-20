import sys
import os.path

def checkCommaValid(string):
    print(string)
    for char in range(len(string)):
        if string[char] == "{" and string[char+1] != '"':
            return [False,4]
        if string[char] == ":" and string[char-1:char+2] != '":"':
            #print('This condition ":"')
            return [False,5]
    if string[-2] == ",":
        return [False,6]
    return [True,0]
fileName = sys.argv[1]
try:
    with open(r'tests\\tests\\step2\\'+fileName,"r") as file:
        data = file.read()
        #print(type(data))
    if len(data) == 0 or (data[0] != "{" or data[-1] != "}"):
        print("Not a valid JSON file")
    if data[-2] == ",":
        print("Not a valid JSON file")
    else:
        print("Valid JSON File")
    print(checkCommaValid(data))
except FileNotFoundError:
    print("File Not Found")
    
print(data)
print(type(data))

