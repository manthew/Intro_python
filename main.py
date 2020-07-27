from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def cal_deriv(ypos, time):
	return -2 * ypos

time_vec = np.linspace(0,4,40)
y = odeint(cal_deriv, y0=1, t=time_vec)

plt.plot(time_vec, y)
plt.show()


