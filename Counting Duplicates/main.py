# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/python
def duplicate_count(text):
    text = text.lower()
    has_check = []
    duplicate = []
    for i in text:
        if i not in has_check:
            has_check.append(i)
        elif i not in duplicate:
            duplicate.append(i)
    return len(duplicate)
print(duplicate_count("Indivisibilities"))