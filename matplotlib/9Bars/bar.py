import matplotlib.pyplot as plt,numpy as np

x = np.array(["Apple", "Bananas", "Pineapple", "Mango"])
y = np.array([45, 350, 20.8, 58])

plt.bar(x,y)
plt.show()

#Horizontal bar

plt.barh(x,y)
plt.title('Horizontal bar')
plt.show()

#bar color

##color cannot be a string; it should be a list
plt.bar(x,y,color=['hotpink','blue','m','#000'])
plt.title('Bar color')
plt.show()

plt.barh(x,y,color=['black'])
plt.title('Bar color(black)')
plt.show()

#bar width(for vertical bar:with bar())
plt.bar(x,y,color=['black'],width=0.5)#default is 0.8
plt.title('Bar width')
plt.show()


#bar height(for horizontal bar:with bhar())
plt.barh(x,y,color=['red'],height=0.9)#default is 0.8
plt.title('Bar height')
plt.show()