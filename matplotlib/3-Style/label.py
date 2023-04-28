import matplotlib.pyplot as plt
import numpy as np
#xlabel,ylabel,title

math = np.array([20, 15, 9,15 , 18, 15, 0, 12,2,5])
cs = np.array([20, 15, 8, 12, 19, 16, 5, 14,5,10])

plt.plot(math, cs)

plt.xlabel("Math marks",label='math')
plt.ylabel("Computer science marks")
plt.title('Math and computer science marks')

plt.show()

#title position(left,center,right)

plt.plot(math, cs)
plt.title('Default')
plt.show()

##left
plt.plot(math, cs)
plt.title('left',loc='left')
plt.show()

##right
plt.plot(math, cs)
plt.title('right',loc='right')
plt.show()

##center(default)
plt.plot(math, cs)
plt.title('center',loc='center')
plt.show()

#font family properties to title and labels

plt.plot(math, cs)

font1 = {'family':'serif','color':'r','size':20}
font2 = {'color':'hotpink','size':15}

plt.title('Relationship', fontdict = font1)
plt.xlabel('Math', fontdict = font2)
plt.ylabel('Computer science', fontdict = font2)

plt.show()

