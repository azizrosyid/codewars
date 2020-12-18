def rot13(message):
    special_characters = " .!@#$%^&*()-+?_=,<>/0123456789"
    result = ""
    for i in message:
        if i in special_characters:
            result += i
            continue
        charNumberElement = i
        charNumberElement = ord(charNumberElement.lower())
        charNumberElement += 13 # menambah 13 character
        charNumberElement = (charNumberElement - 26) if charNumberElement > 122 else charNumberElement
        encoded = chr(charNumberElement)
        if i.isupper():
            encoded = encoded.upper()
        result += encoded
    return result


print(rot13("Akuz anak hebat!"))
print(rot13("OKppkKOAKOkoKA Akoks"))
