def classify(number):
    if number <= 0:
        raise ValueError("Number must be positive and not zero")
    tmp = 0
    for x in range(number):
        if x == 0:
            continue
        if number % x == 0:
            tmp += x

    if tmp == number: return "perfect"
    elif tmp > number: return "abundant"
    else:               return "deficient"
