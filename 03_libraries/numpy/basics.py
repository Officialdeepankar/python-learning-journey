#IT IS BASICALLY USED BECAUSE IT PROVIDES N-D ARRAY 
#IT IS USED INSTEAD OF LIST BECAUSE

# IT USES LESS MEMORY 
# IT IS FAST AND CONVINIENT


import numpy as np
#------------------------------- 1d -------------
a=np.array([1,2,3])  #creating an array object by passing the list [1,2,3]
f=np.array([33,22,35]) 

#-----------------------2D array -------------------


b=np.array([[1,2],[3,4],[5,6]])

print(b.ndim)# shows the diimesnison of the b

#---------------------------------3D array-------------------

c=np.array([
    [     [1,2],
          [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
    ])

print(c[1][1][1])

print("-----------------------------------------------------------------------------")
print(c.shape)
print("-----------------------------------------------------------------------------")

d=np.ones((2,3,3))#initialize with number 1    (dp.zeroes((3,3)))---> initialize with number 0

print(d)

# . arange()-------> initialize list with given range


p=np.arange(0,5)
print("The .arange func. will create this--> ",p)



print("-----------------------------------------------------------------------------")

#   .min(), . max() will give you min and max elememnt of your list or matrix


print("the maximum element of array b is ", b.max())

print("The minimum element of array b is ",b.min())


print("-----------------------------------------------------------------------------")
# .sum () will add all values       

print(b.sum())

#   .sum( axes=0) means add values column wise

print(b.sum(axis=0))# [9,12]

print("-----------------------------------------------------------------------------")
#   .sum( axes=1) means add values row wise
print(b.sum(axis=1))
print("-----------------------------------------------------------------------------")

#  Add two list together 

print(a+f)

print("-----------------------------------------------------------------------------")
#dot product of two matrix 

print(a.dot(f))




# Slicing arrays 
