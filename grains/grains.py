chessboard = []

for x in range(1, 65):
    chessboard.append(x) if x < 3 else chessboard.append(chessboard[x - 2] * 2)

def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Parameter number must be within 1 and 64.")

    return chessboard[number - 1]

def total():
    return sum(chessboard)
