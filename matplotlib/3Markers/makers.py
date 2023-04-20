import matplotlib.pyplot as plt

ycoords=[4,5,8,-20,5.55,4,-7.55]

#circle
plt.plot(ycoords,marker='o')
plt.show()

#star
plt.plot(ycoords,marker='*')
plt.show()

#plus
plt.plot(ycoords,marker='P')
plt.show()

#marker:line:color

plt.plot(ycoords,'P:m')
plt.show()

plt.plot(ycoords,'.:b')
plt.show()

#ms or markersize

plt.plot(ycoords,'o:y',ms=20)
plt.show()

##mec or markeredgecolor

plt.plot(ycoords,markeredgecolor='m',ms=30,marker='o')
plt.show()

##mfc or markerfacecolor

plt.plot(ycoords,markerfacecolor='#4CAF50',ms=30,mec='m',marker='P')
plt.show()

plt.plot(ycoords,markerfacecolor='hotpink',ms=30,mec='m',marker='P')
plt.show()


