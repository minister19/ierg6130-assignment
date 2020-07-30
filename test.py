import numpy as np

print ('--- test ---')

array = np.arange(10)

print(array[:])
print(array.T)
print(array[:].T)
print(array.reshape(5,2))
print(array.reshape(5,2).T)
print(array[:,np.newaxis])
print(array[:,None])
print(array[:,None].T)