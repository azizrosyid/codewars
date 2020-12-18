def to_camel_case(text):
    if len(text) == 0:
        return text
    # your code here
    arrWord = text.split("-")
    for i in range(len(arrWord)):
        arrWord[i] = arrWord[i].split("_")
    newArray = []
    for i in arrWord:
        for j in i:
            newArray.append(j)

    for i in range(len(newArray)):
        newArray[i] = newArray[i].capitalize()
    if not (text[0].isupper()):
        newArray[0] = newArray[0].lower()

    return "".join(newArray)


print(to_camel_case("the_ste-a_lth_warr-ior"))
