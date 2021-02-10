# https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python

def encode_rail_fence_cipher(string, n):
    rail = 0
    mode = "INCREMENT"
    result = {}
    for i in string:
        if str(rail) in result.keys():
            result[str(rail)] += i
        else:
            result[str(rail)] = i
        rail += 1 if mode == "INCREMENT" else -1
        if rail == n-1:
            mode = "DECREMENT"
        elif rail == 0:
            mode = "INCREMENT"
    return "".join(result.values())


def decode_rail_fence_cipher(string, n):
    rail = 0
    mode = "INCREMENT"
    count_char = {}
    for i in string:
        if str(rail) in count_char.keys():
            count_char[str(rail)] += 1
        else:
            count_char[str(rail)] = 1
        rail += 1 if mode == "INCREMENT" else -1
        if rail == n-1:
            mode = "DECREMENT"
        elif rail == 0:
            mode = "INCREMENT"
    list_string = list(string)
    character = {}
    for index,value in enumerate(count_char.values()):
        character[index] = list_string[0:value]
        del list_string[0:value]
    rail = 0
    mode = "INCREMENT"
    result_char = ""
    for i in string:
        result_char+=  character.get(rail).pop(0)
        rail += 1 if mode == "INCREMENT" else -1
        if rail == n-1:
            mode = "DECREMENT"
        elif rail == 0:
            mode = "INCREMENT"
    return result_char



print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3)
      == "WECRLTEERDSOEEFEAOCAIVDEN")
print(encode_rail_fence_cipher("Hello, World!", 3) == "Hoo!el,Wrdl l")
print(encode_rail_fence_cipher("Hello, World!", 4) == "H !e,Wdloollr")
print(encode_rail_fence_cipher("", 3) == "")

print(decode_rail_fence_cipher("H !e,Wdloollr", 4) == "Hello, World!")
print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3)
      == "WEAREDISCOVEREDFLEEATONCE")
print(decode_rail_fence_cipher("", 3) == "")

# decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN",3)

# WECRLTEERDSOEEFEAOCAIVDEN
# WEAREDISCOVEREDFLEEATONCE
# 1232123212321232123212321