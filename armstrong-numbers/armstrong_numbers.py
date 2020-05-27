def is_armstrong_number(number):
    tmp = [int(x) for x in str(number)]
    compar = 0
    for x in tmp:
        compar += pow(x,len(tmp))

    return number == compar
    
    
