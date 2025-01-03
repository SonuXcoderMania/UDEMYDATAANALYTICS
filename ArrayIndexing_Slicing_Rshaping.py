#INDEXING
import numpy as  np


"""array=np.array([18,45,58,66,])
element=array[2]#INDEX POSITION START FROM 0
print("ORIGINAL ARRAY:", array)
print("Element at index:",element)"""

#SLICING
"""array=np.array([18,45,58,66,])
slice_of_araay=array[1:4]#INDEX POSITION START FROM 0
print("ORIGINAL ARRAY:", array)
print("Sliced Element at index:",slice_of_araay)"""

#RESHAPING
#import numpy as np

array = np.array([18, 45, 58, 66,88,65])
reshaped_array = array.reshape(2, 3)  # Reshape to 2x2 array
print("ORIGINAL ARRAY:", array)
print("Reshaped Array (2x2):", reshaped_array)


