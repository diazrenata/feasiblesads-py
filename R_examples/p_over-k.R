library(feasiblesads)

p_lookup <- function(k, s, n) {
  this_p = ps[s - 1, n - (s * k) + 1]
  return(this_p)
}

max_s = 5
max_n = 10


ps <- matrix(ncol = max_n + 1, nrow = max_s)
colnames(ps) <- c(0:max_n)
ps[1, ] = 1
ps[, "0"] = 1
ps[, "1"] = 1
kmax = fill_ks(max_s = max_s, max_n = max_n)

p_over_k <- function(s, n, kmax_table, p_table) {
  sum_p = 0
  this_kmax = kmax_table[s, n + 1]
  for(k in 0:this_kmax) {
    sum_p = sum_p + p_lookup(k, s, n)
  }
  sum_p
}


sum_ps = vector()
p_over_k_ss = vector()
p_over_k_ns = vector()

for(i in 2:nrow(ps)) {
  for(j in 3:ncol(ps)) {
    
    n = j - 1
    p_over_k_ss = c(p_over_k_ss, i)
    p_over_k_ns = c(p_over_k_ns, j)
    
    ps[i,j] = p_over_k(i, n, kmax, ps)
    
  }
}

ps

ps2 <- read.csv(here::here("ps.csv"))

ps_df <- as.data.frame(ps)

ps2 == ps_df


big_ps_r <- fill_ps(50, 1000, FALSE)

big_ps_r_df <- as.data.frame(big_ps_r)

write.csv(big_ps_r_df, "big_ps_r.csv", row.names = F)

big_ps_r_df <- read.csv(here::here("big_ps_r.csv"))
big_ps_python <- read.csv(here::here("big_p_table.csv"))

colnames(big_ps_python) == colnames(big_ps_r_df)
big_ps_r_df <- big_ps_r_df %>%
  mutate_all(.funs = as.double)

big_ps_r_mat <- as.matrix(big_ps_r_df)
big_ps_python_mat <- as.matrix(big_ps_python)

diffmat <- big_ps_r_mat - big_ps_python_mat

sum(diffmat)




library(testthat)
expect_equivalent(big_ps_r_df, big_ps_python)
