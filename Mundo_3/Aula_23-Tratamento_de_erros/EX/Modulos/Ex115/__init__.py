def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo.')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!')


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        linhas = a.readlines()
        a.close()
        return linhas


def cadastrar(nome, idade, arquivo):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write(f'{nome};{idade}\n')
        a.close()
        print(f'Novo registro de {nome} adicionado.')
