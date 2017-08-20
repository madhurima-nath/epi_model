##install packages
install.packages('deSolve')

## Load deSolve package
library(deSolve)

## Create an SIR function
sir <- function(time, state, parameters) {

  with(as.list(c(state, parameters)), {

    dS = -beta * S * I
    dI = beta * S * I - gamma * I
    dR = gamma * I

    return(list(c(dS, dI, dR)))
  })
}

### Set parameters
## Fraction in each compartment: 
## Total population size = N = 1, Infected = 1*10^-5, Susceptibles = N - I, Recovered = 0
N_total = 1
I0 = 1e-05
S0 = N_total - I
R0 = 0.0
init = c(S = S0, I = I0, R = R0)

## beta: infection rate; gamma: recovery rate
parameters = c(beta = 0.5, gamma = 0.05)
## Time frame
days = seq(0, 200, by = 1)

## Solve using ode (General Solver for Ordinary Differential Equations)
out = ode(y = init, times = days, func = sir, parms = parameters)

## change to data frame
out = as.data.frame(out)

## Show data
head(out, 10)

out$time = NULL
## remove the time column from the dataframe, to make it easier to plot


## Plot
fig = matplot(x = days, y = out, type = "l",
        xlab = "Time", ylab = "Fraction of People",
        lwd = 3, lty = 1, bty = "l", col = 2:4)
box(which = "plot")

## Add legend
legend(140, 0.7, c("Susceptible", "Infected", "Recovered"),
       pch = c(NA, NA, NA), lty = 1, col = 2:4, bty = "o", lwd = 3)



