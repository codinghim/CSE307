import re

def checkLegalNumber(input):

    pureNumberFormat = "^[1-9][0-9]*$"
    posNegIntFormat = "^(\+|\-)[1-9][0-9]*$"
    #The latter part after or is there to consider positive or negative sign
    biFormat = "(^(0b|0B)[0-1]+$)|(^(\-|\+)(0b|0B)[0-1]+$)"
    octFormat = "(^(0o|0O)[0-7]+$)|(^(\-|\+)(0o|0O)[0-7]+$)"
    hexFormat = "(^(0x|0X)([0-9]+|[a-f]+|[A-F]+)([0-9]*[a-f]*[A-F]*)*$)|(^(\-|\+)(0x|0X)([0-9]+|[a-f]+|[A-F]+)([0-9]*[a-f]*[A-F]*)*$)" 
    floatFormat = "(^[0-9]*\.[0-9]+$)|(^[0-9]+\.[0-9]*$)|(^(\-|\+)[0-9]*\.[0-9]+$)|(^(\-|\+)[0-9]+\.[0-9]*$)"
    floatSNFormat = "(^[0-9]*\.[0-9]+(e|E)(\-|\+)*[0-9]*$)|(^(\-|\+)[0-9]*\.[0-9]+(e|E)(\-|\+)*[0-9]*$)"

    if re.search(pureNumberFormat, input):
        print("int")
    elif re.search(posNegIntFormat, input):
        print("int")
    elif re.search(biFormat, input):
        print("int")
    elif re.search(octFormat, input):
        print("int")
    elif re.search(hexFormat, input):
        print("int")
    elif re.search(floatFormat, input):
        print("float")
    elif re.search(floatSNFormat, input):
        print("float")
    else:
        print("None")
    #pure numbers
    #binary, octal, hex
    #float
    #scientific notation
    #max float = 1.8 * 10^308. More -> inf
    #
    


while(True):
    x = input("Please enter the legal number: ")
    checkLegalNumber(x)
    exit()