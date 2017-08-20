# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 15:52:30 2017

@author: nmaddy
"""

import networkx as nx
import numpy
import random
import matplotlib.pyplot as plt

G = nx.gnm_random_graph(100,500)
#G = nx.edgelist('foo.txt')

num_sim = 1000       ## number of simulations

inf_rate = 0.5      ## infectionn rate
rec_rate = 1        ## recovery rate

ar = []
atr = []

init = 1            ## number of individuals infected at time t = 0

for m in range(0,num_sim):
    
    n_infected = [1]
    n_susceptible = [G.number_of_nodes()]
    new_infected = []
    n_removed = [0]
    
    state = [0] * (max(G.nodes())+1)

## if any network has some missing nodes, then the following takes care of it
    
    state[0] = 5
    for i in range(len(state)):
        if i not in G.nodes():
            state[i] = 5
    
    infected = random.sample((G.nodes()), init)         ## select one node at random
#    print(infected)
    
    for i in range(len(infected)):
                state[infected[i]] = 1

## the simulation will run as long as the number of infected > 0
    while len(infected) > 0:

        ### Spreading infection
            for j in infected:
                    neighbors = G.neighbors(j)    ## find neighbors of infected node 
                    for k in neighbors:
                        #print k
                        if state[k] == 0 and random.random() < inf_rate:       ## if the neighboring node is not already infected, infect with prob = infected rate
                                    state[k] = 1
                                    new_infected.append(k)
        ### Recovering from infection
            for k in infected[:]:
                if random.random() < rec_rate:          ## for every infected node, change them into recovered state with prob = 1 (recovery rate)
                        state[k] = 2
                        infected.remove(k)         ## remove the recovered nodes from the infected nodes list

            infected = new_infected + infected      ## cumulative number of infected nodes
            new_infected = []                       ## initialize newly infected nodes for every step
            n_infected.append(state.count(1))       ## count the total number of infected nodes (state 1 nodes)
            n_susceptible.append(state.count(0))    ## count the total number of susceptible nodes (state 0 nodes)
            n_removed.append(state.count(2))        ## count the total number of recovered nodes (state 2 nodes)
 
    atr.append(list(n_infected[t]/G.number_of_nodes() for t in range(len(n_infected))))        ## count of the fraction of people infected for each simulation
    ar.append(n_removed[-1]/G.number_of_nodes())    ## the average attack rate for each simulation

print(round(numpy.mean(ar),4))
print(round(numpy.std(ar)/numpy.sqrt(num_sim),4))
## print the mean and the standard deviation of the average attack rate after N number of simulations


atr_mean = [numpy.mean([x[i] for x in atr if len(x) > i]) for i in range(len(max(atr, key = len)))]
## mean of fraction of infected nodes after N simulations

st = [numpy.std([x[i] for x in atr if len(x) > i]) for i in range(len(max(atr, key = len)))]
## standard deviation of fraction of infected nodes after N simulations


for i in range(len(atr)):
    plt.plot(atr[i], color = 'grey')
## plot the epidemic curve for each simulation

plt.errorbar(range(len(atr_mean)), atr_mean, yerr = st/numpy.sqrt(len(max(atr))),
             color = 'black', markersize = 8, ecolor = 'black',
             fmt='-o', markeredgewidth=2, capsize=5, elinewidth=2)
## plot the mean epidemic curve after N simulations with error bars representing the probable error in estimating the mean

plt.xlabel('time')
plt.ylabel('fraction of infected')

