from numpy import loadtxt,arange
import matplotlib.pyplot as plt

data=loadtxt('./company_sales_data.csv',skiprows=1,usecols=arange(0,7),delimiter=',',dtype=int)
months=data[:,0:1].flatten()
face_cream=data[:,1:2].flatten()
face_wash=data[:,2:3].flatten()
tooth_paste=data[:,3:4].flatten()
bathing_soap=data[:,4:5].flatten()
shampoo=data[:,5:6].flatten()
moisturizer=data[:,6:7].flatten()


print(months)



plt.xlabel('Month number')
plt.ylabel('Sales units number')
plt.xticks(months)
plt.yticks([1000, 2000, 4000, 6000,8000,10000,12000,15000,18000])

plt.title('Sales data')
plt.plot(months,face_cream,marker='o',label='Face screem sales data',lw=3)
plt.plot(months,face_wash,marker='o',label='Face wash sales data',lw=3)
plt.plot(months,tooth_paste,marker='o',label='Tooth paste sales data',lw=3)
plt.plot(months,bathing_soap,marker='o',label='Bathing soap sales data',lw=3)
plt.plot(months,shampoo,marker='o',label='Shampoo sales data',lw=3)
plt.plot(months,moisturizer,marker='o',label='Moisturizer sales data',lw=3)

plt.legend(loc='upper left')
plt.show()