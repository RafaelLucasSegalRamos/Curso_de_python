def retornaSoma(a=0, b=0):
    """
    Função que retorna a soma de dois valores
    :param a: int or Float, and if the value of "a" is not passed, it will be 0
    :param b: int or Float, and if the value of "b" is not passed, it will be 0
    :return: The value of a + b
    """
    global c
    c = 10
    return a + b


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# print(input.__doc__)
# print(retornaSoma.__doc__)
s = retornaSoma(2, 7)
print(s)
print(c)

print(fatorial(5))
print(fatorial(4))
print(fatorial(int(input('Digite um número: '))))
print(fatorial())
