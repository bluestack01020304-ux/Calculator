import math

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

def div(a: int | float, b: int | float) -> int | float | str:
    """a와 b를 나누는 함수"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError

    if a==0 or b==0:
        return "0으로 나눌 수 없습니다."

    result = a/b

    if type(result) == float:
        result = math.ceil(result*100)/100

    return result


def toToken(expr: str) -> list:  # float 처리가 안
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
    """계산 함수 args: str
    예시: '5*10+2'"""
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
            tokens[i-1] = div(tokens[i-1], tokens[i+1])  # 결과 type이 달라지면 이후 줄줄이 에러가 나옴
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
