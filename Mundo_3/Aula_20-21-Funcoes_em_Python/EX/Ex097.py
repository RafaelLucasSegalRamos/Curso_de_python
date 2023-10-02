def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'{txt:^{len(txt) + 4}}')
    print('~' * (len(txt) + 4))


texto = str(input('Digite um texto: '))
escreva(texto)