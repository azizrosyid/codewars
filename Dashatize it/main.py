# https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python

def dashatize(n):
    if isinstance(n,int):
        string_n = str(abs(n))
        result = ""
        for i in range(len(string_n)):
            if int(string_n[i]) % 2 == 1:
                if result[-1:] == "-" or len(result) == 0:
                    result += string_n[i]
                else:
                    result += "-" + string_n[i] 
                if i != len(string_n)-1:
                    result+= "-"
            else:
                result+= string_n[i]
        return result
    else:
        return "None"

print(dashatize(274) == "2-7-4")
print(dashatize(5311) == "5-3-1-1")
print(dashatize(86320) == "86-3-20")
print(dashatize(974302) == "9-7-4-3-02")
