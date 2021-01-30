def unique_in_order(iterable):
    result = []
    for index,value in enumerate(iterable):
        if index == 0:
            result.append(value)
        else:
            if iterable[index] != iterable[index-1]:
                result.append(value)
    return result

valid = unique_in_order('AAAABBBCCDAABBB') == ['A','B','C','D','A','B']
print(valid)