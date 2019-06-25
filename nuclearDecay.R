# Copyright (c) 2019, Pietro Vischia pietro.vischia@cern.ch

# Define the pdf

thepdf <- function(t, lambda)
{
        tau<- 1/lambda
        return (1/tau)*exp(-t/tau)
}

xmin<-0
xmax<-5

lambda<-seq(xmin, xmax, len=10000)

# log likelihood is log p(t1, tau)

L <- thepdf(1, lambda)
lnL <- log(thepdf(1, lambda)) -lambda

pdf('figures/nuclearDecay_logL.pdf')
plot(lambda,-2*lnL,type='l',col='blue',xlab=expression(1/tau), ylab='-2 ln(L) (a.u.)', main="Nuclear decay at time t=1", , lty=2, lwd=2)
dev.off()

plot(lambda,thepdf(1, lambda),type='l',col='blue',xlab=expression(1/tau), ylab='Likelihood (a.u.)', main="Nuclear decay at time t=1", , lty=2, lwd=2)

N<- c(..., ..., ..., ...)

for(n in N){
      logL<- 0
      parabola<-0
      for(i in seq_len(n))
            {
                print(i)
                logL = logL + log(thepdf(1,lambda))-lambda
                parabola = parabola + (lambda-1)^2
            }
       myxlim=c(0,5)
       if(n==10) myxlim=c(0.5, 1.5)
       if(n==100) myxlim=c(0.9, 1.1)
       if(n==1000) myxlim=c(0.95, 1.05)
       pdf(paste0('figures/nuclearDecay_approx_',n,'.pdf'))
       plot(lambda,-2*logL-min(-2*logL),type='l',col='blue',xlab=expression(1/tau), ylab='Likelihood (a.u.)', main=paste0("Nuclear decay at time t=1 and N=",n), , lty=2, lwd=2, ylim=c(0,2), xlim=myxlim)
       lines(lambda, parabola, col='black', lty=2, lwd=2)
       
       legend( "topleft", inset=.05, cex = 1, title="",
               c("Exact MLE", "Gaussian approximation"), horiz=FALSE,
               lty=c("dashed","dashed"), lwd=c(2,2),
               col=c("blue","black"), bg="grey96")

       dev.off()
}

