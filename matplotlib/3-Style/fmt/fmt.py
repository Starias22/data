import matplotlib.pyplot as plt

ycoords=[4,5,8,-20,5.55,4,-7.55]

#markerlinecolor

##diamond-line-red
plt.plot(ycoords,'D--r')
plt.show()

##triangle left-dotted-blue
plt.plot(ycoords,'<:b')
plt.show()

##plus-dashed and dotted-green
plt.plot(ycoords,'+-.g')
plt.show()

plt.plot(ycoords,'+-.g',ms=20)
plt.show()








