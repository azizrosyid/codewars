def comp(array1, array2):
    if array2 is not None and array1 is not None:
        array1 = [abs(i) for i in array1]
        for i in array2:
            square_root = i ** 0.5
            if not (square_root in array1):
                return False
            array1.remove(square_root)
        return True
    else:
        return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2) == True)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2) == False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2) == False)

# a1 = None
# a2 = None
# print(comp(a1, a2))
