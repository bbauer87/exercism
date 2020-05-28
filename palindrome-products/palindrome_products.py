def largest(min_factor, max_factor):
    
    palin = calculate(min_factor, max_factor)
    if not palin:
        return (None,[])

    largest_palin = max(palin)
    largest_p_factors = []
    
    for x in range(max_factor, min_factor - 1, -1):
        for y in range(max_factor, min_factor - 1, -1):
            if y * x == largest_palin and [x, y] not in largest_p_factors and [y, x] not in largest_p_factors:
                largest_p_factors.append([x, y])
                break
                
    return (largest_palin, largest_p_factors)


def smallest(min_factor, max_factor):

    palin = calculate(min_factor, max_factor)
    if not palin:
        return (None,[])
    
    smallest_palin = min(palin)
    smallest_p_factors = []  
    
    for x in range(min_factor, max_factor + 1):
        for y in range(min_factor, max_factor + 1):
            if y * x == smallest_palin and [x, y] not in smallest_p_factors and [y, x] not in smallest_p_factors:
                smallest_p_factors.append([x, y])
                break

    return (smallest_palin, smallest_p_factors)

def palindrome(x, y):
    return str(x * y)[::-1] == str(x * y)

def calculate(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("First parameter must be bigger than the second")

    total_products = list(((x * y) for x in range(min_factor, max_factor + 1) for y in range(min_factor, max_factor + 1) if palindrome(x, y)))

    return total_products


## ILoveMuffins solution (https://exercism.io/tracks/python/exercises/palindrome-products/solutions/d68cab86cad94d4d821f26da44bb0722)

##def smallest_palindrome(max_factor, min_factor):
##    return palindrome(min_factor, max_factor)
##
##
##def largest_palindrome(max_factor, min_factor):
##    return palindrome(min_factor, max_factor, smallest=False)
##
##
##def palindrome(mn, mx, smallest=True):
##    args = (mn**2, mx**2+1) if smallest else (mx**2, mn**2-1, -1)
##
##    for r in range(*args):
##        s = str(r)
##        if s == s[::-1] and any(mn <= r//j <= mx
##                for j in range(mn, mx+1) if r % j == 0):
##            return r, ((i, r//i) for i in range(mn, mx + 1)
##                    if r % i == 0 and mn <= i <= r//i <= mx)
##    else:
##        raise ValueError('Could not calculate palindrome for these parameters')
