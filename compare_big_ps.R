library(dplyr)
big_ps_r <- read.csv(here::here("big_ps_r.csv"))
big_ps_py <- read.csv(here::here("big_p_table.csv"))

colnames(big_ps_r)
colnames(big_ps_py)

max(big_ps_r)
max(big_ps_py)

all_equal(big_ps_r, big_ps_py)
