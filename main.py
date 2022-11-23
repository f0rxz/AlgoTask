from typing import List, Tuple


def isHole(c: str):
    return c in '0123456789'


def isLetter(c: str):
    return c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getDistance(letter: Tuple[int, int], hole: Tuple[int, int]):
    return abs(letter[0] - hole[0]) + abs(letter[1] - hole[1])


def number(mapString: str) -> int:

    mapString = mapString.split('\n')

    holes = []
    letters = []
    h = len(mapString)
    w = len(mapString[0])

    # дыры по вертикали
    for y, s in enumerate(mapString):
        if isHole(s[0]):
            holes.append((0, y))

        if isHole(s[-1]):
            holes.append((w - 1, y))

    # дыры по горизонтали
    for x, c in enumerate(mapString[0]):
        if isHole(c):
            holes.append((x, 0))
    for x, c in enumerate(mapString[-1]):
        if isHole(c):
            holes.append((x, h - 1))

    # буквы
    for y, s in enumerate(mapString):
        for x, c in enumerate(s):
            if isLetter(c):
                letters.append((x, y))

    timeInSec = 1
    for letter in letters:
        distance = 1e9 + 7
        for hole in holes:
            distance = min(distance, getDistance(letter, hole))
        timeInSec = max(timeInSec, distance)

    return timeInSec

test = """
+----------------0---------------+
|                                |
|                                |
|          Y        D            |
|     A                          |
|              E                 |
|           N                    |
|  Y                             1
3        Y    D                  |
|         A              X       |
|                                |
+----------------2---------------+
"""[1:-1]

print(number(test))
