

while True:
    try:
        texto = str(input('Digite uma frase: ')).lower()

        print(f'Nesta frase apareceram {texto.count("a")} "a"s')

        print(f'Nesta frase o primeiro "a" apraceu no caractere: {texto.find("a")}')
        print(f'Nesta frase o ultimo "a" apraceu no caractere: {texto.rfind("a")}')



        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico possivel.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
