#!/usr/bin/env python

import scipy.integrate as spi
import numpy as np
import pylab as pl

beta = 0.5 ## infection rate
gamma = 0.05 ## recovery rate

t_inc = 1 ## increament in the number of days 
num_days = 200 ## total number of days to track the infection

## Here it is calculated for the fraction of people. It can be changed to the number of people.
## To change, make N_total = total number of people and I0 = the initial number of infected people
## For example, N_total = 1e6, I_0 = 1.
## This means the total size of the population is 1 million where initially only 1 person is infected.

N_total = 1           ## total population size

I0 = 1e-5             ## initial fraction of infected people
S0 = N_total - I0     ## initial fraction of susceptible people
R0 = 0                ## initial fraction of recovered people

start = (S0, I0, R0)


def diff_eqs(init, t):  
	'''The main set of equations'''
    
	Y = np.zeros((3))     ## initialize the Y-vector with zeros
	V = init              
    
	Y[0] = - beta * V[0] * V[1]
	Y[1] = beta * V[0] * V[1] - gamma * V[1]
	Y[2] = gamma * V[1]
	return Y   # For odeint

t_start = 0.0; t_end = num_days; t_inc = t_inc

t_range = np.arange(t_start, t_end+t_inc, t_inc)

result = spi.odeint(diff_eqs, start, t_range)

print(result) 

## in python 2, print result
## in python 3, print(result)


#Ploting
pl.figure(figsize=(10,10))   ## define figure size

axis_font = {'size':'35', 'color':'black'}
axis_tick_font = {'size':'25', 'color':'black'}

pl.plot(result[:,0], '-b', label='Susceptibles', lw = 3)
pl.plot(result[:,1], '-r', label='Infectious', lw = 3)
pl.plot(result[:,2], '-g', label='Recovered', lw = 3)
pl.legend(loc=0, fontsize = 25)
pl.xlabel('Time', **axis_font)
pl.ylabel('Fraction of People', **axis_font)

pl.xticks(**axis_tick_font)
pl.yticks(**axis_tick_font)

pl.savefig('C:/Users/nmaddy/Documents/git/epi_model/sir.png')

pl.show()


