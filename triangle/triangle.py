def equilateral(sides):
    first = valid(sides)

    return False if not first or sides.count(sides[0]) != len(sides) else True


def isosceles(sides):
    first = valid(sides)

    return True if first and (sides.count(sides[0]) >= 2 or sides.count(sides[1]) >= 2 or sides.count(sides[2]) >= 2) else False

def scalene(sides):
    first = valid(sides)

    return False if not first or sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2] else True

def valid(sides):
    for side in sides:
        if side <= 0:
            return False

    return False if sum(sides[:2]) < sides[2] or sum(sides[1:]) < sides[0] or (sides[0] + sides[2]) < sides[1] else True
        
