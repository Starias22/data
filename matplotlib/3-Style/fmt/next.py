import matplotlib.pyplot as plt

ycoords=[4,5,8,-20,5.55,4,-7.55]

#markerline

## circle-dashed(blue)
plt.plot(ycoords,'o--')
plt.show()

##star-dashed(blue)
plt.plot(ycoords,'*:')
plt.show()

#(no marker)-dashed-red
plt.plot(ycoords,'--r',lw=5)
plt.show()

#plus-(no line)-yellow
plt.plot(ycoords,'Py')
plt.show()

#star-(no line)-(blue)
plt.plot(ycoords,'*')
plt.show()

#(no marker)-(full line)-(cyan)
plt.plot(ycoords,'c')
plt.show()






