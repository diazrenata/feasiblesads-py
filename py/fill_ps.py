import numpy as np
import math as math

def fill_ks(max_s, max_n):
    kmax = np.zeros(shape = [max_s, max_n + 1], dtype = object)
    
    for i in range(max_s):
        for j in range(max_n + 1):
            kmax[i, j] = math.floor(j / (i + 1))
    
    return(kmax)

def p_lookup(k, s, n, ps):
    this_p = int(ps[s - 1, n - ((s + 1) * k) + 1])
    return(this_p)

def p_over_k(s, n, kmax_table, p_table):
    sum_p = int(0)
    this_kmax = kmax_table[s, n + 1]
    
    for k in range(0, this_kmax + 1):
        sum_p = int(sum_p) + int(p_lookup(k, s, n, p_table))
    
    return(sum_p)

def fill_ps(max_s, max_n):
    
    ps = np.zeros(shape = [max_s, max_n + 1], dtype = object)
    ps[0, range(max_n + 1)] = int(1)
    ps[range(max_s), 0] = int(1)
    ps[range(max_s), 1] = int(1)


    kmax = fill_ks(max_s, max_n)
    
    for i in range(1, ps.shape[0]):    
        for j in range(2, ps.shape[1]):
        
            n = j - 1
        
            ps[i, j] = int(p_over_k(i, n, kmax, ps))
    
    return(ps)