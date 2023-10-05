
while True:
    func = str(input('\033[96mFunção ou Biblioteca > [Escreva "FIM" par finalizar o programa] \033[0m')).strip().lower()
    if func == 'fim':
        break
    else:
        print(f'{"~" * 30}\n\033[30:45m{"Sistema de Ajuda PyHelp":^30}\033[0m\n{"~" * 30}')
        print(f'Acessando o manual do comando {func}')
        print(f'\033[30:46m')
        help(func)
        print(f'\033[0m')
print('Até logo!')
