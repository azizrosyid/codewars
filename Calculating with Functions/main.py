def parentNumber(n, number):
    if not n:
        return str(number)
    else:
        n = n.split(" ")
        if n[0] == "+":
            return int(number) + int(n[1])
        elif n[0] == "-":
            return int(number) - int(n[1])
        elif n[0] == "*":
            return int(number) * int(n[1])
        elif n[0] == "/":
            return int(number) // int(n[1])


def zero(n=""): return parentNumber(n, 0)
def one(n=""): return parentNumber(n, 1)
def two(n=""): return parentNumber(n, 2)
def three(n=""): return parentNumber(n, 3)
def four(n=""): return parentNumber(n, 4)
def five(n=""): return parentNumber(n, 5)
def six(n=""): return parentNumber(n, 6)
def seven(n=""): return parentNumber(n, 7)
def eight(n=""): return parentNumber(n, 8)
def nine(n=""): return parentNumber(n, 9)
def plus(n): return f"+ {n}"
def minus(n): return f"- {n}"
def times(n): return f"* {n}"
def divided_by(n): return f"/ {n}"
