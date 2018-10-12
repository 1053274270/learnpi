import numpy as np
y=[1,2,3],[4,5,6],[7,8,9]
a=np.asarray(y)
i,j=10,10
print(a)
for i in range(0,3):
    for j in range(0,3):
        if int(a[i][j])==5:
            print(6)
        else:print(1)
