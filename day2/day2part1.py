# Part 1
course = open("course.txt").read().split("\n")
dirs = {}
for command in course:
    directionAndValue = command.split(" ")
    direction = directionAndValue[0]
    value = int(directionAndValue[1])
    if direction not in dirs:
        dirs[direction] = 0

    dirs[direction] += value
   
res = dirs['forward'] * (dirs['down'] - dirs['up'])    
print(res)