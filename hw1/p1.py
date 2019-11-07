import keyword
import re

def checkIdentifier(input):
    idFormat = '^([a-zA-Z]|_)([a-zA-Z]*_*[0-9]*)*$'
    if not re.search(idFormat,input):
        print("False")
        return False
    elif(keyword.iskeyword(x)):
        print("False")
        return False
    else:
        print("True")
        return True
    #starts with A-Z, a-z, or _ 
    #followed by letters, _, or/and digits
    #cannot be python keywords


while(True):
    x = input("Please enter the identifier: ")
    checkIdentifier(x)
    exit()

