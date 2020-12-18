# def in_array(array1, array2):
#     result = []
#     for i in array2:
#         for j in array1:
#             if j in i:
#                 print(j,i)
#                 result.append(j)

#     result = sorted(list(set(result)))
#     return result

def in_array(array1, array2):
    result = []
    for i in array2:
        for j in array1:
            length = len(j)
            for k in range(len(i)-length+1):
                if j == i[k:length + k]:
                    print(j, i[k:length + k])
                    result.append(j)
                    break
    result = sorted(list(set(result)))
    return result


a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrongentae"]
r = ['arp', 'live', 'strong']
print(in_array(a1, a2))
