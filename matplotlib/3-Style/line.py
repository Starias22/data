import matplotlib.pyplot as plt


ycoords=(2,-2.5,1/3,4.5,8)
#linestyle or ls

plt.plot(ycoords,linestyle='dotted')
plt.show()

plt.plot(ycoords,ls='dashed')
plt.show()

plt.plot(ycoords,ls='--',ms=12,mec='#fff')
plt.show()

plt.plot(ycoords,ls=':',marker='o')
plt.show()


#line width or lw

plt.plot(ycoords,linewidth=20)
plt.show()

plt.plot(ycoords,lw=100)
plt.show()

#multiple lines

plt.plot(ycoords,ls=':',lw=5)
plt.plot((45,8,-20,3.44,20,-9,7,8),lw=2,ls='--')
plt.show()