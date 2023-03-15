

while True:
    try:
        largura = float(input('Digite a largura do cômodo: '))

        height = float(input('Digite a altura do cômodo: '))

        mqua = largura * height

        tinta = mqua / 2

        print(f'Este cômodo possui {mqua} m² e por isso terá que ser usado'
              f' {tinta} litros de tinta para pintar as paredes ')

        break

    except ValueError:
        print('\033[31mUm dos valores não é inteiro, ou float!\033[0m')

    except KeyboardInterrupt:
        print('\033[31mO usuário enterrompeu o programa\033[0m')
        break

    except:
        print('\033[31mHouve um problema que não foi reconhecido pelo sistema.\033[0m')