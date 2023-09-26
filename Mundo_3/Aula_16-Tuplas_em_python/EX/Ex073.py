while True:
    try:

            times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético Mineiro', 'Atlético Paranaense',
                     'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
                     'América Mineiro', 'Chapecoense', 'Vitória', 'Paraná')
            print('-=' * 15)
            print(f'Lista de times do Brasileirão: {times}')
            print('-=' * 15)
            print(f'Os 5 primeiros são: {times[0:5]}')
            print('-=' * 15)
            print(f'Os 4 últimos são: {times[-4:]}')
            print('-=' * 15)
            print(f'Times em ordem alfabética: {sorted(times)}')
            print('-=' * 15)
            print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
            print('-=' * 15)
            print('\033[92mFim do programa.\033[m')

            break


    except KeyboardInterrupt:
        print('\033[91mO usuário decidiu parar o programa.\033[m')
        break
    except Exception as erro:
        print(f'\033[91mO erro que aconteceu foi {erro}\033[m')