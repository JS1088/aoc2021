# Day 5 Part 1
data = open("input.txt").read().split("\n")
matrix = [0 for i in range(1000)]
for i in range(1000):
    matrix[i] = [0 for i in range(1000)]

for line in data:
    row = line.split(" -> ")
    path_from = row[0].split(",")
    path_to = row[1].split(",")
    x_from = min(int(path_from[0]),int(path_to[0]))
    y_from = min(int(path_from[1]),int(path_to[1]))
    x_to = max(int(path_from[0]),int(path_to[0]))
    y_to = max(int(path_from[1]),int(path_to[1]))
    if (x_from == x_to):
        for y in range(y_from, y_to+1, 1):
            matrix[x_from][y]+=1 
    if (y_from == y_to and x_from != x_to):
        for x in range(x_from, x_to+1, 1):
            matrix[x][y_from]+=1 
            
danger = 0  
for row in range(len(matrix)):
    danger+=sum(i >= 2 for i in matrix[row])

print (danger)