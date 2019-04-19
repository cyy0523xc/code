#“罗伯特·菲利普斯, 定价与收益优化. 2008, 北京市: 中国财政经济出版社. 382.”p183中例7.5EMSR-b算法
EMSRb = function(Fare = Fare, Mean = Mean, Var = Var, p_up = numeric(length(Fare)), cap = cap) {
  # ASSURE CONSISTENCY OF THE INPUTS
  tmp <- sort.int(Fare, decreasing=T, method = "sh", index.return=TRUE)
  Fare <- tmp$x
  ind <- tmp$ix
  Mean <- Mean[ind]
  Var <- Var[ind]
  p_up <- p_up[ind]
  # INITIALIZE PROTECTION LEVELS
  p <- vector(mode="numeric", length(Fare))
  for (i in 1:(length(Fare)-1)) {
    # WEIGHTED AVERAGE REVENUE: wr
    wr <- sum(Fare[1:i]*Mean[1:i])/sum(Mean[1:i])
    # MEAN AGGREGATE DEMAND
    X <- sum(Mean[1:i])
    # STANDARD DEVIATION AGGREGATE DEMAND
    Sigma <- sqrt(sum(Var[1:i]))
    # COMPUTE CURRENT PROTECTION LEVEL
    p[i] <- qnorm((1 / (1 - p_up[i+1])) * (1 - Fare[i+1]/wr), mean=X, sd=Sigma)
  } # end for i
  p[length(Fare)] <- cap
  # INTEGER PROTECTION LEVELS
  p <- ceiling(p)
  p <- p * (p < cap) + cap * (p >= cap)
  names(p) <- as.character(Fare)
  return(p)
} # end function


Fare <- c(1050,950,699,520)
Mean <- c(17.3,45.1,39.6,34.0)
Var <- c(5.8,15.0,13.2,11.3)^2
cap <- 130
p <- EMSRb(Fare = Fare, Mean = Mean, Var = Var, cap = cap)
cat("1-N级保护水平分别是：",p)
# 1-N级保护水平分别是： 10 54 97 130
