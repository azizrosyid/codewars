def alphabet_position(text):
    result = []
    for i in text:
        if i.isalpha():
            result.append(ord(i.lower())-96)
    return " ".join([str(x) for x in result])

print(alphabet_position("The sunset sets at twelve o' clock."))