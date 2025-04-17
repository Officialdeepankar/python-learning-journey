
import numpy as np

a=np.arange(0,6).reshape(3,2)

# [[0 1]
#  [2 3]
#  [4 5]]


b=np.arange(6,12).reshape(3,2)


# [[ 6  7]
#  [ 8  9]
#  [10 11]]



#for stacking them in one abvoe the other 


c=np.vstack((a,b))#argument as a tuple

#print(c)

# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]]

d=np.hstack((a,b))# argument as a tuple . this is used to horizontally stack "a" and "b"  together 

print(d)

# [[ 0  1  6  7]
#  [ 2  3  8  9]
#  [ 4  5 10 11]]
