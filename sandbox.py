import sys
import os.path
import re

class JsonParser:
    def __init__(self,fileName):
        
        self.errorCodes = {0:"Valid JSON File",
              1:"JSON file is empty ",
              2:"File Not Found",
              3:"Trailing comma after last key-value pair",
              4:"Preceeding and Trailing braces are absent",
              5:"Key is empty",
              6:"Key is not a string",
              7:"Duplicate Key",
              8:"Value is not in proper format"}
        
        self.successCodes = {
            101:"Basic checks passed",
            102:"Keys are in correct format",
            103:"Values are in correct format"
        }
        
        self.fileName = fileName
        self.data = None
        self.isJson = True
        self.basicCheck = []
        self.keyArr = []
        self.valueArr = []
        self.keyCheckRes = []
        self.valCheckRes = []
    
    def removeExtraSpaces(self,string):
        counter = 0
        for i in range(len(string)):    #remove spaces at the starting
            if string[i] == " ":
                counter += 1
            else:
                break
        string = string[counter:]
        
        counter = len(string) - 1
        for i in range(len(string)-1,-1,-1):    #remove spaces at the end
            if string[i] == " ":
                counter -= 1
            else:
                break
        string = string[:counter+1]
        return string
    
    def dataSplit(self,string): #do basic checks here for upto steps 
        if len(string) == 0:    #if the JSON file is empty
            return [False,1]
        string = self.removeExtraSpaces(string)
        if len(string) == 2 and string != "{}": #self explainatory
            return [False,4]
        if len(string) > 2 and (string[0] != "{" or string[-1] != "}"): #ensure that curly baces are prest at either ends
            return [False,4]
        if len(string) > 2 and string[-2] == ",": #there is comma after last key value pair -> NOT VALID
            return [False,3]
        splitString = re.split(r"[:,]",string[1:-1])  #Remove curly braces and split the string using : and , 
        print(splitString)
        
        keyString = [splitString[x][4:-1] for x in range(len(splitString)) if x%2 == 0]
        for val in range(len(keyString)):
            keyString[val] = self.removeExtraSpaces(keyString[val])
            
        valueString = [splitString[x] for x in range(len(splitString)) if x%2 != 0]
        valueString[-1] = valueString[-1][:-1]
        for val in range(len(keyString)):
            valueString[val] = self.removeExtraSpaces(valueString[val])
        return [True,[keyString,valueString],101]
    
    def keyCheck(self,arr):
        keySet = set()
        for key in arr:
            if key in keySet:
                return[False,7]
            #print(key)
            if key == '':
                return [False,5]
            if not isinstance(key[0],str):
                return [False,6]
        return [True,102]
    
    def valueCheck(self,arr):
        isGood = False
        for value in arr:
            if value in ('""',"''"):    #empty values allowed
                isGood = True
            elif value in ('null'):     #'null' is equal to "null"
                isGood = True
            elif value in ('true','false'):     #boolean values allowed and True,False not allowed
                isGood = True
            elif value.isnumeric():
                isGood = True
            if not isGood:
                return [False,7]
        if isGood:
            return [True,103]
        
        
    def parseJSON(self):
        try:
            with open(r'tests\\tests\\step3\\'+self.fileName,"r") as file:
                self.data = file.read()
                
            self.basicCheck = self.dataSplit(self.data)
            #Do all the basic checks here
            if self.basicCheck[0] is False:
                print("Failing Basic Checks")
                print("Error Code " + str(self.basicCheck[1]) + " " + self.errorCodes[self.basicCheck[1]])
                sys.exit()
            elif self.basicCheck[0] is True:    #basic checks satisfied
                self.keyArr = self.basicCheck[1][0]     #we will get the JSON keys
                self.valueArr = self.basicCheck[1][1]   #we will get the JSON values
                print(self.successCodes[self.basicCheck[2]])
                
            #Now check for JSON keys
            #print(self.keyArr,self.valueArr)
            self.keyCheckRes = self.keyCheck(self.keyArr)
            if self.keyCheckRes[0] is False:
                print("Failing key checks")
                print("Error Code " + str(self.keyCheckRes[1]) + " " + self.errorCodes[self.keyCheckRes[1]])
            elif self.keyCheckRes[0] is True:
                print(self.successCodes[self.keyCheckRes[1]])
                
            #valCheck = self.valueCheck(self.data)
            
            #now we will check if keys are in proper format
                
        except FileNotFoundError:
            print(self.errorCodes[2] + " |     Error Code -" + "2")
        if self.isJson:
            pass
            #print(self.data)

newParser = JsonParser(sys.argv[1])
newParser.parseJSON()