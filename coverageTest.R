n <- 1
conf.level <- 0.95

cover_binom <- function(p) {
  stopifnot(is.numeric(p))
  stopifnot(length(p) == 1)
  stopifnot(0 <= p & p <= 1)
  x <- 0:n
  fpx <- dbinom(x, n, p)
  phat <- x / n
  crit.val <- qnorm((1 + conf.level) / 2)
  low <- phat - crit.val * sqrt(phat * (1 - phat) / n)
  hig <- phat + crit.val * sqrt(phat * (1 - phat) / n)
  inies <- as.numeric(low <= p & p <= hig)
  sum(inies * fpx)
}


cover_clopper <- function(p) {
  stopifnot(is.numeric(p))
  stopifnot(length(p) == 1)
  stopifnot(0 <= p & p <= 1)
  x <- 0:n
  fpx <- dbinom(x, n, p)
  foo <- lapply(x, binom.test, n = n, p = p,
                conf.level = conf.level)
  low <- sapply(foo, function(x) x$conf.int[1])
  hig <- sapply(foo, function(x) x$conf.int[2])
  inies <- as.numeric(low <= p & p <= hig)
  sum(inies * fpx)
}

p <- seq(0.001, 0.999, 0.001)
pdf('figures/coverage_binom.pdf')
plot(p, vapply(p, cover_binom, 0.5), type = "l",
     ylab = "Coverage probability", ylim = c(0.6, 1), col='blue', lwd=2)
lines(p, vapply(p, cover_clopper, 0.5), type='l', col='black', lwd=2)
abline(h = conf.level, lwd=2, col='red', lty = 2)

legend( "bottom", inset=.05, cex = 1, title="",
               c("Binomial", "Clopper-Pearson", "Nominal"), horiz=FALSE,
               lty=c("solid","solid", "dashed"), lwd=c(2,2,2),
               col=c("blue","black","red"), bg="grey96")

dev.off()