from numpy import loadtxt,arange
import matplotlib.pyplot as plt

data=loadtxt('./company_sales_data.csv',skiprows=1,usecols=arange(0,7),delimiter=',',dtype=int)
months=data[:,0:1].flatten()

face_cream=sum(data[:,1:2].flatten())

face_wash=sum(data[:,2:3].flatten())
tooth_paste=sum(data[:,3:4].flatten())
bathing_soap=sum(data[:,4:5].flatten())
shampoo=sum(data[:,5:6].flatten())
moisturizer=sum(data[:,6:7].flatten())


print(months)


sums=[face_cream,face_wash,tooth_paste,bathing_soap,shampoo,moisturizer]
labels=['Face cream','Face wash','Tooth paste','Bathing soap','Shampoo','Moisturizer']
plt.title('Sales data')
plt.pie(sums,labels=labels,autopct='%1.2f%%')#2 digits after,



plt.legend(loc='lower right')
plt.show()