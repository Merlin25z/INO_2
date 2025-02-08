import numpy as np

zeros = np.zeros((8, 8), dtype=int)
for i in range(8):
    for j in range(8):
        if i%2==0:
            if j%2==0:
                zeros[i][j]=1
        else:
            if j % 2 != 0:
                zeros[i][j] = 1


print(zeros)