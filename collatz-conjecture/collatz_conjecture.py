def steps(number):
    if number <= 0: raise ValueError("Parameter must be greater then zero")

    count = 0

    while number != 1:
        number = number * 3 + 1 if number % 2 != 0 else number / 2
        count += 1

    return count
