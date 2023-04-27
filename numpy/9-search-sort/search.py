import numpy as np

a = np.array([12, 90, 380, 12, 211,0,0,25,1,0,-20])

print("a:",a)
print("location of the non-zero elements:",a.nonzero(),sep='\n')


b=np.array([[4,3,1,5],[0,5,6,0],[0,0,2,8]])

print("b:",b,sep='\n')
print("location of the non-zero elements:",b.nonzero(),sep='\n')

b = np.array([12, 90, 380, 12, 211])

print(np.where(b>12))

c = np.array([20, 24,-8,0,21, 23,0,-20])

print('*****',np.where(c<0))

c = np.array([20, 24,-8,0,21, 23,0,-20])

print('*****',np.where(c%2==0))

c = np.array([[20, 24,-8],[0,21, 23],[0,-20,15]])

print('*****',np.where(c<0))