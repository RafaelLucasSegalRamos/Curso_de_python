def leiaint():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def leiafloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n