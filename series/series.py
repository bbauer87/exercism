def slices(series, length):
    if not series or length <= 0 or length > len(series):
        raise ValueError("\nParameter length must be positive and equal or less the size of parameter series (which can't be empty)")

    result = []
    c = 0
    while c < len(series):
        tmp = series[c:]
        add = tmp[:length]
        if len(add) < length:
            break
        result.append(add)
        c += 1
    
    return result

    

    

    
