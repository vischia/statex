import os
import sys
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
from math import sqrt
from statsmodels.stats.proportion import proportion_confint
from itertools import zip_longest
from scipy.optimize import bisect, root

# R qnorm = python .ppf()
# R pnorm = python .cdf()
# R dnorm = python .pmf() (I think)

n=20
conf_level=0.95

def cover_binom(p):
    if not (0 <= p and p <= 1):
        sys.exit()
    x = np.array(range(0, n))
    fpx = ss.binom.pmf(x, n, p)
    phat = x / n
    crit_val = ss.norm.ppf((1 + conf_level) / 2)
    low = [iphat - crit_val * sqrt(iphat * (1 - iphat) / n) for iphat in phat]
    hig = [iphat + crit_val * sqrt(iphat * (1 - iphat) / n) for iphat in phat]
    inies = [ int(ilow <= p and p <= ihig) for ilow, ihig in zip_longest(low, hig) ]
    return sum(inies * fpx)

print(cover_binom(0.6))

#def binomial_ci(mle, N, alpha):
#    to_minimize = lambda c: ss.binom.cdf(mle*N, N, c)-alpha
#    print(mle, N, alpha)
#    print(to_minimize)
#    return bisect(to_minimize, 0, 1)
#    #return root(to_minimize, 0,1)
    
def cover_clopper(p):
    if not (0 <= p and p <= 1):
        sys.exit()
    x = np.array(range(0, n))
    fpx = ss.binom.pmf(x, n, p)
    #foo = [ ss.binom_test(ix, n=n, p=p) for ix in x ]
    #print(proportion_confint(np.array(range(0,n)), n, alpha=conf_level, method="beta"))
    #low = [ binomial_ci(ifoo, n, 1-conf_level) for ifoo in foo ]
    #hig = [ binomial_ci(ifoo, n, conf_level  ) for ifoo in foo ]
    #low = [ ss.beta.ppf(conf_level/2, ix, n-ix +1) for ix in x]
    #hig = [ ss.beta.ppf(1-conf_level/2, ix+1, n-ix) for ix in x]
    low = [ (ss.beta.ppf((1-conf_level)/2, ix, n-ix+1)   )  if ix != 0 else 0 for ix in x]
    hig = [ (ss.beta.ppf(1-(1-conf_level)/2, ix+1, n-ix ))  if ix != n else 1 for ix in x]

    #    ## Determine p s.t. Prob(B(n,p) >= x) = alpha.
    #    ## Use that for x > 0,
    #    ##   Prob(B(n,p) >= x) = pbeta(p, x, n - x + 1).
    #    p.L <- function(x, alpha) {
    #        if(x == 0)                      # No solution
    #            0
    #        else
    #            qbeta(alpha, x, n - x + 1)
    #    }
    #    ## Determine p s.t. Prob(B(n,p) <= x) = alpha.
    #    ## Use that for x < n,
    #    ##   Prob(B(n,p) <= x) = 1 - pbeta(p, x + 1, n - x).
    #    p.U <- function(x, alpha) {
    #        if(x == n)                      # No solution
    #            1
    #        else
    #            qbeta(1 - alpha, x + 1, n - x)
    #}

    
    print("______________", p, "_____________")
    mything = [ (ilow, p, ihig) for ilow, ihig in zip_longest(low, hig) ]
    print(mything)
    inies = [ int(ilow <= p and p <= ihig) for ilow, ihig in zip_longest(low, hig) ]
    print(inies)
    return sum(inies * fpx)

print(cover_clopper(0.6))

p= np.array(np.arange(0.001, 0.999, 0.001))

fix, ax = plt.subplots(1,1)
# pdf('figures/coverage_binom.pdf')
plt.plot(p, [ cover_binom(ip) for ip in p], color="red", linestyle="solid")
plt.plot(p, [ cover_clopper(ip) for ip in p], color="blue", linestyle="solid")
plt.plot(p, [ conf_level for ip in p ], color="black", linestyle="dashed")
plt.show()
#plot(p, vapply(p, cover_binom, 0.5), type = "l",
#     ylab = "Coverage probability", ylim = c(0.6, 1), col='blue', lwd=2)
#lines(p, vapply(p, cover_clopper, 0.5), type='l', col='black', lwd=2)
#abline(h = conf.level, lwd=2, col='red', lty = 2)

#legend( "bottom", inset=.05, cex = 1, title="",
#               c("Binomial", "Clopper-Pearson", "Nominal"), horiz=FALSE,
#               lty=c("solid","solid", "dashed"), lwd=c(2,2,2),
#               col=c("blue","black","red"), bg="grey96")

#dev.off()

