# Day 8 Part 1
data = open("segments.txt").read().split("\n")
count = 0


for line in data:
    output = line.split(" | ")[1]
    for digit in output.split(" "):
        lendigit = len(digit)
        if ((lendigit >=2 and lendigit <=4) or lendigit == 7):
            count+=1
            
print(count)