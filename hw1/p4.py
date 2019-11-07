import datetime
import re

def convertDate(input):
    if checkDateFormat(input) == 1:
        d = datetime.date(int(input[6:10]),int(input[0:2]),int(input[3:5]))
        output = d.strftime("%A, %B %d, %Y")
        return output
    elif checkDateFormat(input) == 0:
        return "Invalid Date Format(MM/DD/YYYY)."
    else:
        return "Invalid date.(MM<12, DD<(29,30, or 31))"

def checkDateFormat(input):
    dateFormat = "^([0-9]{2})/([0-9]{2})/([0-9]{4})$"
    if re.search(dateFormat, input):
        try:
            datetime.date(int(input[6:10]),int(input[0:2]),int(input[3:5]))
        except ValueError:
            return -1
        return 1
    else:
        return 0
    

while(True):
    x = input("Enter the date(MM/DD/YYYY): ")
    output = convertDate(x)
    print(output)
    exit()