def duplicate_encode(word):
    word = [x.lower() for x in word]
    result = ""
    for i in word:
        if word.count(i) > 1:
            result += ")"
        else:
            result += "("
    return result