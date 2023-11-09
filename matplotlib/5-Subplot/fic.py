import matplotlib.pyplot as plt

#subplot function

##plot 1

xcoords=[4,5.33,10,11,13]
ycoords=[-2,5,3,6,-4.4]
plt.subplot(1,2,1)
plt.plot(xcoords,ycoords)
##plot 2
xcoords=[4,5,6]
ycoords=[2,3,6]
plt.subplot(1,2,2)
plt.plot(xcoords,ycoords)

plt.show()

# subplot titles

xcoords=[4,5.33,10,11,13]
ycoords=[-2,5,3,6,-4.4]
##plot 1
plt.subplot(2,1,1)
plt.title('Sublot1',loc='right')
plt.plot(xcoords,ycoords)
##plot 2
xcoords=[4,5,6]
ycoords=[2,3,6]
plt.subplot(2,1,2)
plt.title('Sublot2',loc='left')
plt.plot(xcoords,ycoords)
# subplot super title
plt.suptitle('Super title')
plt.show()
# Many subplots

import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.suptitle('Super title')

plt.show()


