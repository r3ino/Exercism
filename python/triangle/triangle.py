def equilateral(sides):
    inequality = sides[0] + sides [1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]

    return sides[1] == sides[2] == sides[0] and sum(sides) != 0 and inequality


def isosceles(sides):
    inequality = sides[0] + sides [1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]

    return (sides[1] == sides[2] or sides[1] == sides[0] or sides[2] == sides[0]) and inequality


def scalene(sides):
    inequality = sides[0] + sides [1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]

    return sides[1] != sides[2] and sides[1] != sides[0] and sides[0] != sides[2] and inequality
