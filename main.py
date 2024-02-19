import sys
import os.path
errorCodes = {0:"Valid JSON File",
              1:"Invalid JSON File",
              2:"File Not Found",
              3:"Trailing comma after last key-value pair"}
fileName = sys.argv[1]
data = None
isJson = True
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
    if isJson:
        print("0")
except FileNotFoundError:
    print(errorCodes[2] + " |     Error Code -" + "2")
if isJson:
    print(data)