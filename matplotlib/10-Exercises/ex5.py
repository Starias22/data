from numpy import loadtxt,arange
import matplotlib.pyplot as plt

data=loadtxt('./company_sales_data.csv',skiprows=1,usecols=(0,1,2),delimiter=',',dtype=int)
#print(len(data))

months=data[:,0:1].flatten()

face_cream=data[:,1:2].flatten()
face_wash=data[:,2:3].flatten()





plt.xlabel('Month number')
plt.ylabel('Sales units number')
plt.xticks(months)
#plt.yticks(arange(4500,8001,step=500))

plt.title('Facewash and facecream Sales data')


plt.bar([m-0.25 for m in months],face_cream,label='Face Cream Sales data',width=0.25,align='edge')
plt.bar([m+0.25 for m in months],face_wash,label='Face Wash Sales data',width=0.25,align='edge')

plt.legend(loc='upper left')
plt.grid(ls='--')
plt.show()