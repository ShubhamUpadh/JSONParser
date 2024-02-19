import sys
import os.path


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
except FileNotFoundError:
    print("File Not Found")
    
print(data)
print(type(data))

