import numpy as np

#amin and amax
arr=np.array([44,55,66,-20])
arr2=np.array([44,55,56,57,58])

mat=np.array([[4,5,6],[3,2,9],[-20,44,33],[20,30,44]])#4*3 array
print(np.amin([4,-3,6,7,0.55]))
print(np.amin((0,454,99,-20,33)))
print(np.amax([2,5,6,0,5]))
print(np.amax((-20,55,99)))

print(np.amin(arr))
print(np.amax(arr))

print(np.amin(mat))
print(np.amax(mat))


print(np.amin(mat,axis=0))
print(np.amin(mat,axis=1))

print(np.amax(mat,axis=0))
print(np.amax(mat,axis=1))

#mean
print(np.mean(arr))
print(np.sum(arr)/arr.size)

print(np.mean(mat))
print(np.sum(mat)/mat.size)

print(np.mean(mat,axis=0))
print(np.sum(mat,axis=0)/mat.shape[0])

print(np.mean(mat,axis=1))
print(np.sum(mat,axis=1)/mat.shape[1])

# Weighted mean

print(np.average(arr))
print(np.average(arr,weights=[1,6,3,5]))
print(np.average(mat))
print(np.average(mat,weights=[[1,6,3],[1,2,3],[4,2,9],[4,5,6]]))
print(np.average(mat,axis=0))
print(np.average(mat,axis=0,weights=[1,5,6,7]))
print(np.average(mat,axis=1,weights=[5,-2,7]))



#median
print(np.mean(arr))
print(np.median(arr2))

print(np.median(mat))
print(np.median(mat,axis=0))
print(np.median(mat,axis=1))

#variance

print(np.var(arr))
print(np.var(mat))
print(np.var(mat,axis=0))
print(np.var(mat,axis=1))

#standard deviation
print(np.std(arr))
print(np.std(mat))
print(np.std(mat,axis=0))
print(np.std(mat,axis=1))

# range
print(np.ptp(arr))

#percentile

print(np.percentile(arr,10,0))
#correlation

x=[1,2,3,4]
y=[-20,5,6,9]
## covariance
print(np.cov(x,y))
## correlation coefficcient
np.corrcoef(x,y)

