def stock_list(listOfArt, listOfCat):
    result = {}
    for i in listOfArt:
        elem = i.split(' ')
        if elem[0][0] in result.keys():
            result[elem[0][0]] += int(elem[1])
        else:
            result[elem[0][0]] = int(elem[1])
    
    if len(set(result.keys()).intersection(set(listOfCat))) == 0:
        return ""
    strResult = ""
    for i in listOfCat:
        if i in result.keys():
            strResult += f"({i} : {result[i]}) - "
        else:
            strResult += f"({i} : 0) - "
    return strResult[:-3]


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["F", "G"]
print(stock_list(b, c))