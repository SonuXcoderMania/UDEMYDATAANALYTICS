import numpy as np

import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])

'''element_2d = array_2d[1,2]
element_3d=array_3d[1,0,1]

print(element_2d)
print(element_3d)'''

slice_2d=array_2d[:,1:3]
slice_3d=array_3d[1,:,:]

print(slice_2d)
print(slice_3d)



