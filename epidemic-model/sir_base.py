import matplotlib.pylab as plt
from scipy.integrate import odeint
import numpy as np

### SIR base model
def model(eq, sir0, t):
	sir = odeint(eq, sir0, t)
	return sir
### differential equations
def diff(sir, r0=0.25, gamma=1./14):
	beta = r0*gamma
	N = np.sum(sir)
	# sir[0] == S, sir[1] == I, sir[2] == R
	dsdt = - (beta * sir[0] * sir[1])/N
	didt = (beta * sir[0] * sir[1])/N - gamma * sir[1]
	drdt = gamma * sir[1]
	print (dsdt + didt + drdt)
	dsdidr = [dsdt, didt, drdt]
	return dsdidr
