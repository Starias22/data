import numpy as np

print(np.pi)
print(4*np.e)
print(np.nan)
print(np.inf)
print(-np.inf)

arr = np.array([0, 30, 60, 90, 120, 150, 180])
print("\nThe sin value of the angles",end = " ")
print(np.sin(arr * np.pi/180))
print("\nThe cosine value of the angles",end = " ")
print(np.cos(arr * np.pi/180))
print("\nThe tangent value of the angles",end = " ")
print(np.tan(arr * np.pi/180))

print(np.degrees(2*np.pi))

print(np.radians(180))
#sin cos tan
#sinh cosh tanh
#arcsinh arccosh arctanh
#arcsin arccos arctan

import numpy as np
arr = np.array([12.202, 90.23120, 123.020, 23.202])
print("printing the original array values:",end = " ")
print(arr)
print("Array values rounded off to 2 decimal position",np.around(arr, 2))
print("Array values rounded off to -1 decimal position",np.around(arr, -1))

print(np.floor(41.5))
print(np.ceil(44.5))
arr = [0.23, 0.09, 1.2, 1.24, 9.99]

print("Input array:",arr)

r_arr = np.fix(arr)

print("Output array:",r_arr)
print(np.hypot(4,3))

arr = [0, 45, 90, 30 ]
print ("Input array : \n", arr)




r_arr = np.trunc(arr)

print("Truncated array:",r_arr)

r_arr = np.rint(arr)

print("Output array:",r_arr)

radval = np.deg2rad(arr)
print ("\n Radian value : \n", radval)

arr = [0, np.pi/4, np.pi/2, np.pi/6 ]
print ("Input array : \n", arr)

degval = np.rad2deg(arr)
print ("\n Degree value : \n", degval)