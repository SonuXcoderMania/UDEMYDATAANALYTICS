#BASIC OPERATIONS
import numpy as np

array1=np.array([1,8,3,4,5])
array2=np.array([4,5,6,55,7])
result_add=array1+array2
result_multi=array1*array2
comparision =array1>array2
print("Comparision:",comparision)
print(result_add)
print(result_multi)
scaler=5 #IT IS USED TO ADD VALUE IN PARTICULAR ELEMENT LIST/ARRAY ETC
result_broadcast=array1+scaler
print("Broadcasting result:",result_broadcast)# THAT IS KNOWN AS BROADCASTING