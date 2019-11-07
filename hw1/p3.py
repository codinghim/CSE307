import re

def checkEscape(input):
    startString = ""
    backslashCounter = 0
    backslashflag = -2
    counter = 0
    for ch in input:
        if backslashflag == (counter-1):
            if ch == "\\":
                backslashflag = counter
                backslashCounter = backslashCounter + 1
            else:
                backslashCounter = 0
        elif ch == '\\':
            backslashCounter = 0
            backslashflag = counter
            backslashCounter = backslashCounter + 1
        if(counter == len(input)-1):
            if (backslashCounter % 2) != 0:
                return 1
            else:
                return 0
        counter = counter + 1

def checkLegalString(input1, input2):
    #print(checkEscape(input1))
    backSlashFormat = "^\\+$"
    if checkEscape(input1):
        #print(input1)
        #print(backSlashFormat)
        #print(re.search(backSlashFormat,input1))
        if re.search(backSlashFormat,input1):
            input = input2
        else:
            input = input1 + input2
    else:
        if input2 != "":
            #print("False: escaped and not empty")
            return 0
        else:
            input = input1
    #print("input is " + input)
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
                #print("false: not starting with quote")
                return 0

        if counter == len(input)-1:
            if ch != startString:
                #print("False: ending not match")
                return 0

        if backslashflag == (counter-1):
            if ch == startString:
                if counter == len(input)-1:
                    #print("False: ending with escaped startstring")
                    return 0
        elif ch == '\\':
            backslashflag = counter
        elif counter !=0 and counter != len(input)-1 and ch == startString:
            #print("False: duplicate quotes")
            return 0

        counter = counter + 1
    #print("True")
    return 1
    


while(True):
    x = input("Please enter the line 1: ")
    y = input("Please enter the line 2: ")

    if checkLegalString(x,y):
        print("True")
    else:
        print("False")
    exit()
