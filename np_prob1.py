import numpy as np
import random                #import random module
m=int(input("enter m : "))   #take input m from user

n=int(input("enter n : "))
x=np.random.random((m,n)) 
np.savetxt("bks.txt",x)  # save the data of x in bks.txt file
np.loadtxt("bks.txt")   # load the the file 

