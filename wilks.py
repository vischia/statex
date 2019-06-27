# Credit to https://stephens999.github.io/fiveMinuteStats/wilks.html for the original R version of this script
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math
n_pseudoexperiments = 100
# True value of the parameter
lam = 0.4
n_observations = [ 10, 100 ]

for nsampl in n_observations:
    samples = np.zeros(n_pseudoexperiments)
    print("Running pseudoexperiments for {nsampl} observations".format(nsampl=nsampl))
    for toy in range(1, n_pseudoexperiments):
        print("      Toy # {toy}".format(toy=toy))
        # Sample nsampl observations from a Poisson(0.4)   
        pseudodata   = np.random.poisson(size=nsampl, lam=lam)
        print(nsampl)
        print(pseudodata)
        print(lam)
        print(mean(pseudodata))
        print(mean(pseudodata)//lam)
        # Logarithm operation fails because the argument is zero
        # the argument is zero because mean(pseudodata) is zero
        # however, computing it from the python console from the same array
        # gives the correct non-zero value. !?!!?!??!
        samples[toy] = 2*nsampl*(mean(pseudodata)*math.log(mean(pseudodata)/lam) + lam - mean(pseudodata))
                       
    fix, ax = plt.subplots(1,1)
    #pdf(paste0('figures/wilks_',nsampl,'.pdf'))
    plt.hist(samples, color="black")
    plt.xlabel("Sampled values of log-likelihood ratio values")
    plt.ylabel("Frequency")
    plt.title("Log-likelihood ratio")
    x = np.linspace(0,20)
    plt.plot(x,ss.chi2.pdf(x,1))
    plt.show()

