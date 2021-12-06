binary = open("binary.txt").read().split("\n")
res_arr = []
res_arr = [0 for i in range(12)] 
lines = 0;
for line in binary:
    lines+=1
    pos = 0
    for char in line:
        res_arr[pos]+=int(char)
        pos+=1
        
gamma = [1 if int(i)>lines/2 else 0 for i in res_arr]
epsilon = [1 if int(i)<lines/2 else 0 for i in res_arr]

dec_gamma = int("".join(str(x) for x in gamma), 2)
dec_epsilon = int("".join(str(x) for x in epsilon), 2)

res = dec_gamma * dec_epsilon
print(res)