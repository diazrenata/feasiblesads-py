from fill_ps import *
import pandas as pd
import random as random
import numpy as np

def send_gnome(s, n, ps, ks):
    

    this_gnome = [0] * s

    if s == 1:
        return(this_gnome)
    
    slots_remaining = s
    n_remaining = n
    
    current_size = 0
    
    for species_slot in range(s):
        
        # final species slot
        
        if species_slot == s - 1:
            
            this_gnome[species_slot] = current_size + n_remaining
            break
        
        if species_slot == 0:
            
            # first species value is a boundary case
            # for the first, the values of n range from 1 to ks[s, n + 1]
            
            ns = list(range(1,ks[slots_remaining - 1, n_remaining]))
            
        else: 
                
            # for the rest, the values of n range from 0 to ks[slots_remaining, n_remaining + 1]

            ns = list(range(0, ks[slots_remaining - 1, n_remaining]))
        
        # the probability of selecting each n is proportional the the number of partitions possible were you to choose that n, divided by the total number of possible partitions across all possible choices for n.
        n_parts = ps[slots_remaining - 2, ([n_remaining - (x*slots_remaining) for x in ns])]
        
        # total partition size
        total_parts = sum(n_parts)
        
        # probability of each n choice
        p_ns = n_parts / total_parts
        
        this_increment = random.choices(ns, weights = p_ns, k = 1)
        
        current_size = current_size + this_increment[0]
        this_gnome[species_slot] = current_size
        n_remaining = n_remaining - (slots_remaining * this_increment[0])
        slots_remaining = slots_remaining - 1
    
    return(this_gnome)
    
def sample_fs(s, n, nsamples, p_table = None):
    
    if p_table is None:
        
        p_table = fill_ps(s, n)
    
    ks = fill_ks(s, n)
    
    sets = np.zeros(shape = [nsamples, s], dtype = int)
    
    for idx in range(nsamples):
        
        sets[idx, ] = send_gnome(s, n, p_table, ks)
        
    return(sets)

def tally_sets(fs_samples):
    
    values, counts = np.unique(fs_samples, return_counts = True, axis  = 0)

    values_df = pd.DataFrame(values)
    
    values_df["frequency"] = counts
    
    return(values_df)