# Day 3 Part 2
binary = open("binary.txt").read().split("\n")
matrix = [0 for i in range(len(binary))]
res_arr = [0 for i in range(12)] 
line_arr = [0 for i in range(12)] 
row = 0;
for line in binary:
    pos = 0
    for char in line:
        line_arr[pos]=int(char)
        res_arr[pos]+=int(char)
        pos+=1
        
    matrix[row] = [int(i) for i in line_arr]
    row+=1

matrix_orig = [list(i) for i in matrix]
res = [0 for i in range(2)]

for round in range(2):
    matrix = [list(i) for i in matrix_orig]
    for bit_pos in range(len(line_arr)):
        if (len(matrix)>1):       
            matrix_reduced = []
            target = 0
            if (round==0):
                target = 1 if (res_arr[bit_pos]>=len(matrix)/2) > 0 else 0
            else:
                target = 0 if (res_arr[bit_pos]>=len(matrix)/2) > 0 else 1 

            for row in range(len(matrix)):
                if matrix[row][bit_pos] == target:
                    matrix_reduced.append(matrix[row])

            res_arr = [sum(x) for x in zip(*matrix_reduced)]
            matrix = [list(i) for i in matrix_reduced]

    res[round] = "".join(str(x) for x in matrix[0])
    

print(int(res[0],2)*int(res[1],2))   