from numpy import loadtxt,arange
import matplotlib.pyplot as plt

data=loadtxt('./company_sales_data.csv',skiprows=1,usecols=[0,2,4],delimiter=',',dtype=int)
months=data[:,0:1].flatten()

face_wash=data[:,1:2].flatten()
bathing_soap=data[:,2:3].flatten()



print(months)
print(face_wash)
print(bathing_soap)



#plt.yticks([1000, 2000, 4000, 6000,8000,10000,12000,15000,18000])


plt.subplot(2,1,1).set_title('Sales data of bathing soap')
plt.plot(months,bathing_soap,marker='o',color='black',lw=3)

plt.subplot(2,1,2).set_title('Sales data of Face wash')
plt.plot(months,face_wash,marker='o',color='r',lw=3)

plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.xticks(months)

plt.show()