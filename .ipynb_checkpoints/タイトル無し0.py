# -*- coding: utf-8 -*-
import numpy as np
import scipy.optimize
import matplotlib.pylab as plt

# data which you want to fit
xdata = np.array([0.0,1.0,2.0,3.0,4.0,5.0,6.0])
ydata = np.array([0.1,0.9,2.2,2.8,4.2,5.9,7.4])
# initial guess for the parameters
parameter_initial = np.array([0.0, 0.0, 0.0]) #a, b, c
# function to fit
def func(x, a, b, c):
    return a + b*x + c*x*x

paramater_optimal, covariance = scipy.optimize.curve_fit(func, xdata, ydata, p0=parameter_initial)
print ("paramater =")
print (paramater_optimal)

y = func(xdata,paramater_optimal[0],paramater_optimal[1],paramater_optimal[2])
plt.plot(xdata, ydata, 'o')
plt.plot(xdata, y, '-')
plt.show()