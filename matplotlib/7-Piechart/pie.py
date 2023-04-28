import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])


plt.pie(y)
plt.title('My first pie chart',loc='right')
plt.show()

#labels
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.title('A pie chart with label',loc='right')
plt.show()

# start angle

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

#colors

mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, startangle = 90,colors=mycolors)
plt.show()

#explode

myexplode = [0.2, 0, 0, 0]

mycolors = ["blue", "hotpink", "m", "#4CAF50"]
plt.pie(y, labels = mylabels, startangle = 20.55,colors=mycolors,explode=myexplode)
plt.show()

#shadow

plt.pie(y, labels = mylabels, startangle = 20.55,colors=mycolors,explode=myexplode,shadow=True)#default False
plt.show()

#legend

plt.pie(y, labels = mylabels, startangle = 20.55,colors=mycolors,explode=myexplode)
plt.legend()
plt.show()

##with header
plt.pie(y, labels = mylabels, startangle = 20.55,colors=mycolors,explode=myexplode)
plt.legend(title='Header of the legend')
plt.show()
