import matplotlib.pyplot as plt

ycoords=[4,5,8,-20,5.55,4,-7.55]


#star
plt.plot(ycoords,marker='*')
plt.show()

#plus
plt.plot(ycoords,marker='P')
plt.show()

#ms or markersize

plt.plot(ycoords,ms=20)
plt.show()

##mec or markeredgecolor

plt.plot(ycoords,markeredgecolor='m',ms=30,marker='o')
plt.show()

##mfc or markerfacecolor

plt.plot(ycoords,markerfacecolor='#4CAF50',ms=30,mec='m',marker='P')
plt.show()

plt.plot(ycoords,mfc='hotpink',ms=30,mec='m',marker='P')
plt.show()


