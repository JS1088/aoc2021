# Day 8 Part 1
data = open("segments.txt").read().split("\n")

def splitstr(word):
    return [char for char in word]

def sortstr(word):
    sorted_digit = sorted(word)
    sorted_digit_string = ''.join(sorted_digit)
    return sorted_digit_string

total = 0
for line in data:
    res = {}
    output = line.split(" | ")[0]
    code = line.split(" | ")[1]
    while (len(res)<10):
        for digit in output.split(" "):
            digit = sortstr(digit.strip())
            lendigit = len(digit)
            digit_list = splitstr(digit)
            if (lendigit == 2): 
                res[1] = digit
            if (lendigit == 3):
                res[7] = digit
            if (lendigit == 4):
                res[4] = digit
            if (lendigit == 7):
                res[8] = digit  
            if (7 in res and lendigit == 5 and all(item in digit_list for item in splitstr(res[7]))):
                res[3] = digit
            if (4 in res and lendigit == 6 and all(item in digit_list for item in splitstr(res[4]))):
                res[9] = digit
            if (3 in res and 9 in res and lendigit == 5 and all(item in splitstr(res[9]) for item in digit_list) and digit != res[3] ):
                res[5] = digit
            if (8 in res and 5 in res and lendigit == 5 and digit != res[5] and digit != res[3]):
                res[2] = digit
            if (5 in res and 9 in res and lendigit == 6 and all(item in digit_list for item in splitstr(res[5])) and digit != res[9] ):
                res[6] = digit
            if (9 in res and 6 in res and lendigit == 6 and digit != res[9] and digit != res[6]):
                res[0] = digit  
    zahl = ''  
    for digit in code.split(" "):
        digit = digit.strip() 
        sorted_digit = sortstr(digit)
        for value in res:
            if (res[value]==sorted_digit):
                zahl = zahl + f'{value}' 

    total += int(zahl)
    
print(total)    