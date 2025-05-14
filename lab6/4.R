set.seed(0)
library(boot)

rsq_function <- function(formula, data, indices) {
  d <- data[indices,]
  fit <- lm(formula, data = d)
  return(summary(fit)$r.square)
}

reps <- boot(data = mtcars, 
            statistic = rsq_function, 
            R = 2000, 
            formula = mpg ~ disp)

pe <- rsq_function(mpg ~ disp, mtcars, 1:nrow(mtcars))

par(mfrow = c(1, 2))

hist(reps$t, 
     main = "Бутстрап R-квадрата",
     xlab = "R-квадрат",
     col = "lightblue",
     border = "white")
abline(v = pe, col = "red", lwd = 2, lty = 2)
abline(v = boot.ci(reps, type = "perc")$percent[4:5], 
       col = "darkgreen", lty = 3, lwd = 2)

plot(mpg ~ disp, 
     data = mtcars,
     main = "Исходные данные",
     pch = 19, col = "blue")
abline(lm(mpg ~ disp, data = mtcars), 
       col = "red", lwd = 2)

cat("Результаты:\n")
cat("Точечная оценка R-квадрата:", round(pe, 3), "\n")
ci <- boot.ci(reps, type = "perc")
cat("95% ДИ: [", round(ci$percent[4], 3), ",", 
    round(ci$percent[5], 3), "]\n")