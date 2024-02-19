import sys
import os.path
import json

fileName = sys.argv[1]
try:
    with open(r'tests\\tests\\step1\\'+fileName,"r") as file:
        data = json.load(file)
        print(type(data))
except json.JSONDecodeError:
    print("Invalid JSON file")
except FileNotFoundError:
    print("File Not Found")
    
#print(type(data))

