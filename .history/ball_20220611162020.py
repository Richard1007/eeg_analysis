MAX = 100;
 
# table to store to store results of subproblems
dp = [[[[-1] * 4 for i in range(MAX)]
                 for j in range(MAX)]
                 for k in range(MAX)]
print(dp)