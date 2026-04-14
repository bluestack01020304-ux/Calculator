def add(a: int, b: int) -> int:
    """a와 b를 더하는 함수"""
    if type(a) != int or type(b) != int: raise TypeError
    return a + b

def sub(a: int, b: int) -> int:
    """a와 b를 빼는 함수"""
    if type(a) != int or type(b) != int: raise TypeError
    return a - b

def mult(a: int, b: int) -> int:
    """a와 b를 곱하는 함수"""
    if type(a) != int or type(b) != int: raise TypeError
    return a * b

def div(a: int, b: int) -> int:
    """a와 b를 나누는 함수"""
    if type(a) != int or type(b) != int: raise TypeError
    return a / b



def toToken(expr: str) -> list:
    tokens = []
    temp = ""

    for c in expr:
        if c.isalnum():   # 숫자 또는 문자
            temp += c
        else:
            if temp:
                tokens.append(temp)
                temp = ""
            tokens.append(c)

    if temp:
        tokens.append(temp)

    return tokens


def calcul(expr: str):

    tokens = toToken(expr)

    # 숫자 변환
    for i, v in enumerate(tokens):
        if v.isdigit():
            tokens[i] = int(v)

    # 1단계 * /
    i = 0
    while i < len(tokens):
        if tokens[i] == "*":
            tokens[i-1] = mult(tokens[i-1], tokens[i+1])
            del tokens[i:i+2]
            i -= 1
        elif tokens[i] == "/":
            tokens[i-1] = div(tokens[i-1], tokens[i+1])
            del tokens[i:i+2]
            i -= 1
        else:
            i += 1

    # 2단계 + -
    i = 0
    while i < len(tokens):
        if tokens[i] == "+":
            tokens[i-1] = add(tokens[i-1], tokens[i+1])
            del tokens[i:i+2]
            i -= 1
        elif tokens[i] == "-":
            tokens[i-1] = sub(tokens[i-1], tokens[i+1])
            del tokens[i:i+2]
            i -= 1
        else:
            i += 1

    return tokens[0]