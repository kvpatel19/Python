from matplotlib import pyplot as plt
import numpy as np
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.axis('equal')
langs=['c','c++','java','python','php']
students=[23,17,35,29,12]
ax.pie(students,labels=langs,autopct='%1.2f%%')
plt.show()
