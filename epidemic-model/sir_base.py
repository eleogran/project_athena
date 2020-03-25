import matplotlib.pylab as plt
from scipy.integrate import odeint
import numpy as np

### SIR base model
def model(eq, sir0, t):
	sir = odeint(eq, sir0, t)
	return sir
### differential equations
def diff(sir, beta=0.18, gamma=1./14):
	# beta = contact rate = R0 * gamma (with R0 = 2.5)
	# gamma = mean recovery rate (in 1/days).
	N = np.sum(sir)
	# sir[0] - S, sir[1] - I, sir[2] - R
	dsdt = - (beta * sir[0] * sir[1])/N
	didt = (beta * sir[0] * sir[1])/N - gamma * sir[1]
	drdt = gamma * sir[1]
	print (dsdt + didt + drdt)
	dsdidr = [dsdt, didt, drdt]
	return dsdidr

#Italy 3/24/20
#confirmed deaths recovered active
#69176	6820	8326	54030