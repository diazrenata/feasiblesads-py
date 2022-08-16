def simpson_diversity(an_sad):
    total_n = sum(an_sad)
    denominator = total_n * (total_n - 1)
    
    numerator_vector = [0] * len(an_sad)
    
    for i in range(len(an_sad)):
        numerator_vector[i] = an_sad[i] * (an_sad[i] - 1)
        
    numerator = sum(numerator_vector)
    
    diversity = 1 - (numerator / denominator)
    
    return(diversity)