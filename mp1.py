import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0,6.0,0.01)
plt.plot(x,[i**2 for i in x])
plt.plot(x,[i*2 for i in x])
plt.plot(x,[1/i for i in x])
plt.show()
