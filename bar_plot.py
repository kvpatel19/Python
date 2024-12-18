import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
langs=['c','c++','java','python','php']
students=[23,17,35,29,12]
ax.bar(langs,students)
plt.show()
