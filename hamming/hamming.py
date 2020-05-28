def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Error! The sequences must have equal length.")

## first way I thought it (tests 0.016s):
    dif = 0
    for x , y in zip(strand_a , strand_b):
        if x != y:
            dif += 1
            
    return dif

## a more elegant way, but the tests were a little slower (0.078s):
##    return sum([1 if x != y else 0 for x , y in zip(strand_a, strand_b)])
