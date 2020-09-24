import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,4*np.pi,0.2)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)','cosx(x)'])
plt.show()
