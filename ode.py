"""Solve the position as a function of time for Morse potential"""
import numpy as np
from scipy import integrate

def ode(Y, t):
    a = 1
    m = 1
    D = 1
    return [Y[1],2*(a/m)*D*np.exp(-2*a*Y[0])*(1-np.exp(a*Y[0]))]

a_t = np.arange(0,10,0.01)
asol = integrate.odeint(ode, [1,0],a_t)

np.savetxt("morse_disp.dat",asol[:574,0])
#import matplotlib.pyplot as plt
#plt.plot(a_t,asol[:,0])
#plt.show()
