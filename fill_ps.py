import numpy as np
import math as math

def fill_ks(max_s, max_n):
    kmax = np.zeros(shape = [max_s, max_n + 1], dtype = int)
    
    for i in range(max_s):
        for j in range(max_n + 1):
            kmax[i, j] = math.floor(j / (i + 1))
    
    return(kmax)

def p_lookup(k, s, n, ps):
    this_p = ps[s - 1, n - ((s + 1) * k) + 1]
    return(this_p)

def p_over_k(s, n, kmax_table, p_table):
    sum_p = 0
    this_kmax = kmax_table[s, n + 1]
    
    for k in range(0, this_kmax + 1):
        sum_p = sum_p + p_lookup(k, s, n, p_table)
    
    return(sum_p)

def fill_ps(max_s, max_n):
    
    ps = np.full(shape = [max_s, max_n + 1], fill_value= np.nan)
    ps[0, range(max_n + 1)] = 1
    ps[range(max_s), 0] = 1
    ps[range(max_s), 1] = 1


    kmax = fill_ks(max_s, max_n)
    
    for i in range(1, ps.shape[0]):    
        for j in range(2, ps.shape[1]):
        
            n = j - 1
        
            ps[i, j] = p_over_k(i, n, kmax, ps)
    
    return(ps)