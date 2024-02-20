import sys
import os.path
errorCodes = {0:"Valid JSON File",
              1:"Invalid JSON File",
              2:"File Not Found",
              3:"Trailing comma after last key-value pair"}
fileName = sys.argv[1]
data = None
isJson = True
def checkCommaValid(string):
    for char in range(len(string)):
        if string[char] == "{" and string[char+1] != '"':
            return [False,4]
        if string[char] == ":" and string[char-1:char+2] != '":"':
            #print('This condition ":"')
            return [False,5]
    return [True,0]
try:
    with open(r'tests\\tests\\step2\\'+fileName,"r") as file:
        data = file.read()
        #print(type(data))
    if len(data) == 0 or (data[0] != "{" or data[-1] != "}"):
        print(errorCodes[1] + " |     Error Code -" +"1")
        isJson = not isJson
    if data[-2] == ",":
        print(errorCodes[3] + " |     Error Code -" +"1")
        isJson = not isJson
    if checkCommaValid(data)[0] is False:
        print(checkCommaValid(data))
    if isJson:
        print("0")
except FileNotFoundError:
    print(errorCodes[2] + " |     Error Code -" + "2")
if isJson:
    print(data)