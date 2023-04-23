import numpy as np
vect1=np.array([10,8,5,7,3,2])
vect2=np.array([5,6,8,-9,-3,-4])
print('-vect1',-vect1)
print('+vect1',+vect1)
print('2*vect2',2*vect2)
print('vect2*3',vect2*3)
print('5+vect1',5+vect1)
print('(vect1)+1',vect1+1)
print('(vect1)-10',vect1-10)
print('(vect1)//8',vect1//8)
#the dtype can change

print('(vect2)/3',vect2/3)
print('dtype',(vect2/3).dtype)
print('100/vect2',100/vect2)
print('100//vect2',100//vect2)
print('100%vect2',100%vect2)
print('(vect2)%3',vect2%3)
print('(vect2)**3',vect2**3)
print('4**vect1',4**vect1)
#print('vect1/0',vect1/0)



print('vect1+vect2:',vect1+vect2)
print('vect1-vect2:',vect1-vect2)
print('vect1*vect2:',vect1*vect2)
print('vect1//vect2:',vect1//vect2,)
print('vect1/vect2:',vect1/vect2,sep='\n')
#print('vect1**vect2:',vect1**vect2,sep)
print('vect1%vect2:',vect1%vect2)
print('vect2**vect1:',vect2**vect1)
print('4+2*vect1%vect2:',4+2*vect1%vect2)

mat1=np.array([[4,2,6],[1,2,6],[4,2,-2]])
mat2=np.array([[2,2,-1],[1,0,6],[0,2,3]])
mat=mat1*mat2
print('mat1:',mat1,sep='\n')
print('mat2:',mat2,sep='\n')
print('mat1*mat2:',mat,sep='\n')
print('mat1**2:',mat1**2,sep='\n')
f6=np.full((3,3),46)
print('f6:',f6)
print('10%2+2*mat1+mat2-9+f6//2:',2*mat1+mat2-9,sep='\n')








