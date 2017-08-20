# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:23:28 2016

@author: madhurima
"""

import networkx as nx
import random
import numpy

def main():
    
    ''' This function gives the value of the overall average attack
        rate after a user specified number of simulations for 
        a given value for the infected rate'''
    
    num_sim = 1000                      ## number of simulations
    p = 0.5                             ## infection rate
        
    G = nx.gnm_random_graph(100, 500)

    N = G.number_of_nodes()
    
    tot_episize = []
    
    for i in range(num_sim):
        sg = [edge for edge in G.edges() if random.random() < p]     ## selectes edges at random
        #print(sg)             
        sub_graph = nx.Graph(sg)           ## make a sub-graph using those edges
                      
        a = sorted(nx.connected_components(sub_graph), key = len, reverse=True)       ## sort the connected components in descending order
#        print(a)
        episize = sum([len(x)**2 for x in a])/float(N**2)
        tot_episize.append(episize)

    print(round(numpy.mean(tot_episize),4))
    print(round(numpy.std(tot_episize),4))
    return tot_episize
main()

 
