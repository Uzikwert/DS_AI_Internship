#Task 1: The Normalizer
import numpy as np
print("TASK 1")
original=np.random.randint(50,100,size=[5,3])
m=np.mean(original,axis=0)
print("Mean scores:\n",m)
centered=original-m
print("Original Scores:\n",original)
print("Centered Scores:\n",centered)
#Task 2: The Reshaper
print("TASK 2")
og=np.arange(24)
reshaped=og.reshape(4,3,2)
transposed=reshaped.transpose(0,2,1)
print("Final Shape:\n",transposed.shape)
print("Final Array:\n",transposed)