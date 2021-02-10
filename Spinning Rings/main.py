# https://www.codewars.com/kata/59afff65f1c8274f270020f5/train/python
def spinning_rings(inner_max, outer_max):
    inner = 0
    outer = 0
    action = 0
    while True:
        inner = decrementStay(inner, 0, inner_max)
        outer = incrementStay(outer, 0, outer_max)
        action +=1
        if inner == outer:
            break
    return action


def decrementStay(now, min, max):
    return now - 1 if now -1 >= min else max


def incrementStay(now, min, max):
    return now + 1 if now + 1 <= max else min


print(spinning_rings(2, 3))
print(spinning_rings(3, 2))
print(spinning_rings(1, 1))
print(spinning_rings(2, 2))
print(spinning_rings(3, 3))
