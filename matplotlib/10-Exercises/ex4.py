from numpy import loadtxt,arange
import matplotlib.pyplot as plt

data=loadtxt('./company_sales_data.csv',skiprows=1,usecols=(0,3),delimiter=',',dtype=int)
#print(len(data))

months=data[:,0:1].flatten()

tooth_paste=data[:,1:2].flatten()



print(months)
print(tooth_paste)



plt.xlabel('Month number')
plt.ylabel('Sales units number')
plt.xticks(months)
#plt.yticks(arange(4500,8001,step=500))
print(arange(4500,8001,step=500))

plt.title('Tooth paste Sales data')


plt.scatter(months,tooth_paste,label='Tooth paste Sales data',s=50)
plt.legend(loc='upper left')
plt.grid(ls='--')
plt.show()