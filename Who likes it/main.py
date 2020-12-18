def likes(names):
    numberNames = len(names)
    if numberNames == 0:
        return 'no one likes this'
    elif numberNames == 1:
        return f"{names[0]} likes this"
    elif numberNames == 2:
        return f"{names[0]} and {names[1]} like this"
    elif numberNames == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif numberNames >= 4:
        return f"{names[0]}, {names[1]} and {numberNames - 2} others like this"


print(likes(['Peter']))
