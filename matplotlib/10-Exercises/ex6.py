from numpy import loadtxt,arange
import matplotlib.pyplot as plt

data=loadtxt('./company_sales_data.csv',skiprows=1,usecols=(0,4),delimiter=',',dtype=int)
#print(len(data))

months=data[:,0:1].flatten()
bathing_soap=data[:,1:2].flatten()






plt.xlabel('Month number')
plt.ylabel('Sales units in number')
plt.xticks(months)
#plt.yticks(arange(4500,8001,step=500))

plt.title('Bathing soap Sales data')


plt.bar(months,bathing_soap,width=0.8,align='center')

plt.grid(ls='--')
plt.savefig('bathsoap.pdf')
plt.savefig('bathsoap.png')
plt.savefig('bathsoap.jpg')
plt.savefig('bathsoap.jpeg')
plt.savefig('bathsoap.svg')
"""plt.savefig(fname, dpi=None, facecolor='w', edgecolor='w', orientation='portrait',
            format=None, transparent=False, bbox_inches=None, pad_inches=0.1,
            metadata=None, **kwargs)"""



plt.show()
