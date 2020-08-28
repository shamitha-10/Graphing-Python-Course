import matplotlib.pyplot as plt
import numpy as np
import math

l=1
g=9.8
T=(2*math.pi)*(math.sqrt(l/g))
t=[]
a=np.arange(0,90,1)

for i in a:
    t.append(T)

plt.plot(a,t)
plt.show()

