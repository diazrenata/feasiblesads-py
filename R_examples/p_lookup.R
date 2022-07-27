library(feasiblesads)

p_lookup <- function(k, s, n) {
  this_p = ps[s - 1, n - (s * k) + 1]
  return(gmp::as.bigz(this_p))
}

max_s = 5
max_n = 10

ps <- matrix(ncol = max_n + 1, nrow = max_s)
colnames(ps) <- c(0:max_n)
ps[1, ] = 1
ps[, "0"] = 1
ps[, "1"] = 1
kmax = fill_ks(max_s = max_s, max_n = max_n)

ps <- matrix(ncol = max_n + 1, nrow = max_s)
colnames(ps) <- c(0:max_n)
ps[1, ] = 1
ps[, "0"] = 1
ps[, "1"] = 1
kmax = fill_ks(max_s = max_s, max_n = max_n)

p_lookup <- function(k, s, n) {
  this_p = ps[s - 1, n - (s * k) + 1]
  return(this_p)
}

kmaxs = vector()
ss = vector()
ns = vector()
ks = vector()
p_rows = vector()
p_cols = vector()
p_lookups = vector()

for(i in 2:nrow(ps)) {
  
  # print(as.vector(kmax[i, ]))
  for(j in 3:ncol(ps)) {
    print(as.numeric(kmax[i, j]))
    n = j - 1
 
    
    for(k in 0:(kmax[i, n + 1])) {
      kmaxs = c(kmaxs, (kmax[i, n + 1]))
      ss = c(ss, i)
      ns = c(ns, j)
      ks = c(ks, k)
      p_rows = c(p_rows, i -1)
      p_cols = c(p_cols, n - (i * k) + 1)
      p_lookups = c(p_lookups, ps[i - 1, n - (i * k) + 1])
    }
    
  }
}

p_rows

ps[p_rows[1], p_cols[1]]

indices_R <- data.frame(s = ss, n = ns, k = ks, prow = p_rows, pcol = p_cols, p_lookedup = p_lookups)
indices <- read.csv(here::here("indices.csv"))

library(dplyr)

indices <- indices %>%
  mutate(s_R = s + 1,
         n_R = n + 1,
         prow_R = p_row + 1,
         pcol_R = p_col + 1)

indices_compare <- indices %>%
  select(s_R,
         n_R,
         k,
         prow_R,
         pcol_R,
         p_lookedup)

indices_R == indices_compare

which(is.na(indices_R$p_lookedup)) == which(is.na(indices$p_lookedup))      
