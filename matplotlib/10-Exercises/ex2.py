from numpy import loadtxt
import matplotlib.pyplot as plt

data=loadtxt('./company_sales_data.csv',skiprows=1,usecols=(0,-1),delimiter=',',dtype=int)
months=data[:,0:1].flatten()
sales=data[:,1:2].flatten()
print(months)
print(sales)


plt.xlabel('Month number')
plt.ylabel('Sold units number')
plt.xticks(months)
plt.yticks([100000, 200000, 300000, 400000, 500000])
#plt.axis([1,12,100000,500000])
plt.title('Company sales data of last year')
plt.plot(months,sales,'o--r',label='Profit data of last year',lw=3,mfc='black')
plt.legend(loc='lower right')
plt.show()