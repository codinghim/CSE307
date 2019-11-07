import re

def checkLegalString(input):
    backslashflag = -2
    counter = 0
    StringFormat = "(^\"\"$)|(^\'\'$)"
    startString = ""
    backslashCounter = 0
    for ch in input:
        if counter == 0:
            if ch == "\"":
                startString = "\""
            elif ch == "\'":
                startString = "\'"
            else:
                print("False")
                return -1
        if counter == len(input)-1:
            if ch != startString:
                print("False")
                return -1
        if backslashflag == (counter-1):
            if ch == "\'":
                if counter == len(input)-1:
                    print("False")
                    return -1
            elif ch == "\"":
                if counter == len(input)-1:
                    print("False")
                    return -1
            #elif ch == "\\":
            #else:
        elif ch == '\\':
            backslashflag = counter
        counter = counter + 1
    print("True")
    
    


while(True):
    x = input("Please enter the line 1: ")
    y = input("Please enter the line 2: ")
    #if x=="exit":
        #exit()
    checkLegalString(x+y)
    exit()