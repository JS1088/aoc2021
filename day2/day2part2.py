# Part 2
course = open("course.txt").read().split("\n")
depth = 0
forward = 0;
aim = 0;
for command in course:
    directionAndValue = command.split(" ")
    direction = directionAndValue[0]
    value = int(directionAndValue[1])
    
    if (direction == "forward"):
        forward += value
        depth += aim*value
    else:
        aim = (aim + value) if direction == 'down' else (aim - value)
   
res = forward * depth    
print(res)