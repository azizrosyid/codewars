# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
def narcissistic(value):
    result = 0
    str_value = str(value)
    for i in str_value:
        result += int(i) ** len(str_value) 
    return value == result 


print(narcissistic(7) == True)
print(narcissistic(371) == True)
print(narcissistic(122) == False)
print(narcissistic(4887) == False)
