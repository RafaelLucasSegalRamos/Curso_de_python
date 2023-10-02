def titulo(txt):
    txt = txt.strip().upper()
    print("-" * len(txt) + "-" * 30)
    print(f"{txt:^{len(txt) + 30}}")
    print("-" * len(txt) + "-" * 30)


def soma(a, b):
    s = a + b
    print(f"A soma de {a} + {b} = {s}")


def somaindefinida(*valores):
    s = 0
    for n in valores:
        s += n
    print(f"A soma dos valores {valores} = {s}")


titulo("CURSO EM VIDEO")
titulo("APRENDA PYTHON")
titulo("TESTando")
titulo("paralelepipedo")

soma(4, 5)
somaindefinida(8, 9, 6, 7, 8, 9, 0, 1, 2, 21, 2, 32, 43, 4, 5, 345, 64, 646, 456)

soma(b=4, a=5)