from numpy import loadtxt
import matplotlib.pyplot as plt

data=loadtxt('./company_sales_data.csv',skiprows=1,usecols=(0,-1),delimiter=',',dtype=int)
months=data[:,0:1].flatten()
profits=data[:,1:2].flatten()

print(months)
print(profits)

profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.xlabel('Profit data')
plt.ylabel('Actual profit in dollar')


plt.xticks(profit_range)

#plt.axis([1,12,100000,500000])
plt.title('Profit range in dollar')
plt.hist(profits,profit_range,label='Profit data')

plt.legend(loc='upper left')

plt.show()