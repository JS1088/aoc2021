# Day 5 Part 2
data = open("input.txt").read().split("\n")
matrix = [0 for i in range(1000)]
for i in range(1000):
    matrix[i] = [0 for i in range(1000)]

for line in data:
    row = line.split(" -> ")
    path_from = row[0].split(",")
    path_to = row[1].split(",")
    x_from = int(path_from[0])
    y_from = int(path_from[1])
    x_to = int(path_to[0])
    y_to = int(path_to[1])
    if (x_from == x_to):
        for y in range(min(y_from,y_to), max(y_to,y_from)+1, 1):
            matrix[x_from][y]+=1 
    if (y_from == y_to and x_from != x_to):
        for x in range(min(x_from,x_to), max(x_to,x_from)+1, 1):
            matrix[x][y_from]+=1 
    if (abs(x_from - x_to) == abs(y_from - y_to)):
        if (x_from < x_to) and (y_from < y_to):
            for i in range(abs(x_from - x_to)+1):
                matrix[x_from+i][y_from+i]+=1
        elif (x_from < x_to) and (y_from > y_to):
            for i in range(abs(x_from - x_to)+1):
                matrix[x_from+i][y_from-i]+=1
        elif (x_from > x_to) and (y_from < y_to):
            for i in range(abs(x_from - x_to)+1):
                matrix[x_from-i][y_from+i]+=1
        elif (x_from > x_to) and (y_from > y_to):
            for i in range(abs(x_from - x_to)+1):
                matrix[x_from-i][y_from-i]+=1
            
danger = 0  
for row in range(len(matrix)):
    danger+=sum(i >= 2 for i in matrix[row])

print (danger)