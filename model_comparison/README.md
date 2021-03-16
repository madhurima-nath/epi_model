# Epidemic Modeling
### Problem statement:  
Given various network models which represent interaction between people, test the efficacy for predicting disease outbreak on the actual data.

For this particular case, I worked with survey data from school students where they were asked to identify their friends with whom they interact regularly.

### Type of Data Used:
I used graphs/networks to represent the population, where the nodes represent the individual and the interactions are the edges.

All the networks representing the social interactions, are undirected and unweighted with 1460 vertices and 974 edges. The node id's represent the students, unique for each student.
The node id's are integers.

### Actions:
1. Generate network from actual survey data
2. Generate random networks with similar properties as the actual data
3. Compared the structure of the random networks to the actual data
	- calculated average degree
	- calculated the degree distribution - tells about the distribution of the neighbours of an individual
	- calculated different centrality measures - closeness and betweenness centrality
	- calculated clustering coefficients
4. Simulated disease model S-I-R (Susceptible-Infected-Recovered) using python
	- fraction of infected individuals over the coirse of the epidemic
	- overall average attack rate (new cases divided by the total population)
5. Compared the disease outbreak in the networks
	- graphically
	- t-test

### Hypothesis:
A model captures the underying social interactions the best gives the best prediction for disease outbreak.
    
### Results and Analysis:
1. Values of average degree for the networks
2. Plots of degree distribution
3. Plots of centrality measures - closeness and betweenness
4. Plots of clustering coefficients
5. Results from the S-I-R simulations
    - Plots of fraction of infected individuals as a function of time
    - Table showing the values of the overall average attack rate
6. Comparison - Results from t-test


## References:
1. Handcock M, Hunter D, Butts C, Goodreau S, Krivitsky P, Bender-deMoll S and Morris M (2016). statnet: Software Tools for the Statistical Analysis of Network Data.
The Statnet Project (http://www.statnet.org). R package version 2016.9, CRAN.R-project.org/package=statnet.

2. Handcock M, Hunter D, Butts C, Goodreau S and Morris M (2008). “statnet: Software Tools for the Representation, Visualization, Analysis and Simulation of Network Data.” 
Journal of Statistical Software, 24(1), pp. 1–11. http://www.jstatsoft.org/v24/i01.

3. Resnick, Michael D., et al. "Protecting adolescents from harm: findings from the National Longitudinal Study on Adolescent Health." Jama 278.10 (1997): 823-832.

4. Nath, Madhurima, et al. "Determining whether a class of random graphs is consistent with an observed contact network." Journal of theoretical biology 440 (2018): 121-132.

