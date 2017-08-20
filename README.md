This repository contains codes for simple SIR model (no births, no deaths). It has a compartmental model (both in python and R) and one for SIR simulation. The files will do some basic plots for the number of people infected, recovered as well. The SIR simulations will generate epidemic curves.


The simple SIR compartmental model can be expressed as the following set of equations:

<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dS(t)}{dt}&space;=&space;-&space;\frac{\beta&space;I(t)&space;S(t)}{N}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dS(t)}{dt}&space;=&space;-&space;\frac{\beta&space;I(t)&space;S(t)}{N}" title="\frac{dS(t)}{dt} = - \frac{\beta I(t) S(t)}{N}" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dI(t)}{dt}&space;=&space;\frac{\beta&space;I(t)&space;S(t)}{N}-\gamma&space;I(t)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dI(t)}{dt}&space;=&space;\frac{\beta&space;I(t)&space;S(t)}{N}-\gamma&space;I(t)" title="\frac{dI(t)}{dt} = \frac{\beta I(t) S(t)}{N}-\gamma I(t)" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dR(t)}{dt}&space;=&space;\gamma&space;I(t)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dR(t)}{dt}&space;=&space;\gamma&space;I(t)" title="\frac{dR(t)}{dt} = \gamma I(t)" /></a>

This model was proposed by Kermack and McKemndrick. The three variables - **_S(t), I(t)_** and **_R(t)_** - represent the number of people in each compartment, **_susceptibles, infected_** and **_recovered_**, at a particular time. Also, the total population size **_N_** remains constant. It follows that 

<a href="http://www.codecogs.com/eqnedit.php?latex=S(t)&space;&plus;&space;I(t)&space;&plus;&space;R(t)&space;=&space;\text{constant}&space;=&space;N" target="_blank"><img src="http://latex.codecogs.com/gif.latex?S(t)&space;&plus;&space;I(t)&space;&plus;&space;R(t)&space;=&space;\text{constant}&space;=&space;N" title="S(t) + I(t) + R(t) = \text{constant} = N" /></a>

Further, the dynamics depends on the ratio

<a href="http://www.codecogs.com/eqnedit.php?latex=R_0&space;=&space;\frac{\beta}{\gamma}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?R_0&space;=&space;\frac{\beta}{\gamma}" title="R_0 = \frac{\beta}{\gamma}" /></a>

which is called the **_basic reproduction ratio_**.

## References
1. Contributions to the mathematical theory of epidemics--I. 1927, Kermack WO, McKendrick AG. https://www.ncbi.nlm.nih.gov/pubmed/2059741
