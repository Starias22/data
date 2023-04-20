import matplotlib.pyplot as plt

y=[4,45,2,5,6,7,8,10]

plt.plot(y,marker='o')
plt.title('An example')
plt.xlabel('x-coordinates')
plt.ylabel('ycoordinates')
plt.grid()
plt.show()

#Grid axis:x,y,both

##x axis
plt.plot(y,marker='o')
plt.title('An example')
plt.xlabel('x-coordinates')
plt.ylabel('ycoordinates')
plt.grid(axis='x')
plt.show()

##y axis
plt.plot(y,marker='o')
plt.title('An example')
plt.xlabel('x-coordinates')
plt.ylabel('ycoordinates')
plt.grid(axis='y')
plt.show()

##both(default)
plt.plot(y,marker='o')
plt.title('An example')
plt.xlabel('x-coordinates')
plt.ylabel('ycoordinates')
plt.grid(axis='both')
plt.show()

#Grid line properties

plt.plot(y,marker='o')
plt.title('An example')
plt.xlabel('x-coordinates')
plt.ylabel('ycoordinates')
plt.grid(axis='both',ls='--',lw=2.5,color='hotpink')
plt.show()