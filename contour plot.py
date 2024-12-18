import numpy as np
import matplotlib.pyplot as plt
xlist=np.linspace(-3.0,3.0,100)
ylist=np.linspace(-3.0,3.0,100)
x,y=np.meshgrid(xlist,ylist)
z=np.sqrt(x**2+y**2)
fig,ax=plt.subplots(1,1)
cp=ax.contourf(x,y,z)
fig.colorbar(cp)
ax.set_title('filled contourf plot')
ax.set_ylabel('y(cm)')
plt.show()
