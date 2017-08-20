This repository contains codes for simple SIR model (no births, no deaths). It has a compartmental model (both in python and R) and one for SIR simulation. The files will do some basic plots for the number of people infected, recovered as well. The SIR simulations will generate epidemic curves.


The simple SIR compartmental model can be expressed as the following set of equations:

![eqn1] (https://www.latex4technics.com/l4ttemp/brx713.png?1503242545197)
![eqn2] (https://www.latex4technics.com/l4ttemp/brx713.png?1503242580770)
![eqn3] (https://www.latex4technics.com/l4ttemp/brx713.png?1503242608479)

This model was proposed by Kermack and McKemndrick. The three variables - ** _S(t), I(t)_ ** and ** _R(t)_ ** - represent the number of people in each compartment, ** _susceptibles, infected_ ** and ** _recovered_ **, at a particular time. Also, the total population size **_N_** remains constant. It follows that ![eqn4] (https://www.latex4technics.com/l4ttemp/brx713.png?1503242207497)

Further, the dynamics depends on the ratio
![eqn5] (https://www.latex4technics.com/l4ttemp/brx713.png?1503242292403) 
which is called the **_basic reproduction ratio_**.

## References
1. Contributions to the mathematical theory of epidemics--I. 1927, Kermack WO, McKendrick AG. [link text itself]: https://www.ncbi.nlm.nih.gov/pubmed/2059741
