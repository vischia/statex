# Credit to https://stephens999.github.io/fiveMinuteStats/wilks.html for the original version of this script

n_pseudoexperiments         <- ...
# True value of the parameter
lambda           <- 0.4
n_observations <- c(..., ..., ...)

for(nsampl in n_observations){
           samples <- numeric(n_pseudoexperiments)
           print(paste0("Running pseudoexperiments for ",nsampl, " observations"))
           for(toy in seq_len(n_pseudoexperiments)) {
                    print(paste0("      Toy #", toy))
                    # Sample nsampl observations from a Poisson(0.4)   
                    pseudodata      <- rpois(nsampl, lambda)
                    samples[toy]   <- 2*nsampl*(mean(pseudodata)*log(mean(pseudodata)/lambda) + lambda - mean(pseudodata))
                    }                   
           pdf(paste0('figures/wilks_',nsampl,'.pdf'))
           my<-hist(samples, freq=F, main='Log-likelihood ratio', xlab='Sampled values of log-likelihood ratio values', type='l')
           myc<-curve(dchisq(x, 1), 0, 20, lwd=2, xlab = "", ylab = "", add = T)
           dev.off()
}
