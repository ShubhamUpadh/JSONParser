import sys
import os.path

class JsonParser:
    def __init__(self,fileName):
        
        self.errorCodes = {0:"Valid JSON File",
              1:"Invalid JSON File",
              2:"File Not Found",
              3:"Trailing comma after last key-value pair",
              4:"Key not a string",
              5: ""}
        
        self.fileName = fileName
        self.data = None
        self.isJson = True
        self.checkCommaValidValue = []
        
    def checkCommaValid(self,string):
        for char in range(len(string)):
            if string[char] == "{" and string[char+1] not in ('"',"}"):
                return [False,4]
            if string[char] == ":" and string[char-1:char+2] != '":"':
                #print('This condition ":"')
                return [False,4]
        return [True,0]
    
    def parseJSON(self):
        try:
            with open(r'tests\\tests\\step2\\'+self.fileName,"r") as file:
                self.data = file.read()
                #print(type(data))
            if len(self.data) == 0 or (self.data[0] != "{" or self.data[-1] != "}"):
                print(self.errorCodes[1] + " |     Error Code -" +"1")
                self.isJson = not self.isJson
            if len(self.data) > 2 and self.data[-2] == ",":
                print(self.errorCodes[3] + " |     Error Code -" +"1")
                self.isJson = not self.isJson
            self.checkCommaValidValue = self.checkCommaValid(self.data)
            if self.checkCommaValidValue[0] is False:
                print(self.errorCodes[self.checkCommaValidValue[1]] + " |     Error Code -" + str(self.checkCommaValidValue[1]))
                self.isJson = not self.isJson
            if self.isJson:
                print("0")
        except FileNotFoundError:
            print(self.errorCodes[2] + " |     Error Code -" + "2")
        if self.isJson:
            print(self.data)

newParser = JsonParser(sys.argv[1])
newParser.parseJSON()