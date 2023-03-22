# A definição do \033[m pode ser \033[style;text;backgroud;m,
# mas os valores podem ser colocados em qualquer ordem que não alterára o resultado final

print('\033[0;33;44mUm exemplo de código com estilo\033[0m')
# cor amarela, fundo azul e nenhum estilo

# Estes são valores para o estilo(style) do texto
print('\033[0mUm exemplo de código com estilo\033[0m')  # Texto padrão
print('\033[1mUm exemplo de código com estilo\033[0m')  # Texto em negrito
print('\033[2mUm exemplo de código com estilo\033[0m')  # Texto esmaecido
print('\033[3mUm exemplo de código com estilo\033[0m')  # Texto em italico
print('\033[4mUm exemplo de código com estilo\033[0m')  # Texto com underline(linha embaixo do texto)
print('\033[5mUm exemplo de código com estilo\033[0m')  # Deixa o Texto piscante
print('\033[7mUm exemplo de código com estilo\033[0m')  # Inverte a cor de fundo com a cor do texto
print('\033[8mUm exemplo de código com estilo\033[0m')  # Teoricamente deixa o texto invisivel

print('\n\033[1;4;7mUm exemplo de código com estilo\033[0m')  # tambem é possivel combinar estilos.

print('\n\u2713 exemplo de código com estilo')
# O \u#### Coloca em pequeno simbolo onde quer que foi colocado o \u

# Estes são valores para cores de texto:

print('\n\033[30mUm exemplo de código com estilo\033[0m')  # Texto cor PRETO
print('\033[31mUm exemplo de código com estilo\033[0m')  # Texto cor VERMELHO
print('\033[32mUm exemplo de código com estilo\033[0m')  # Texto cor VERDE
print('\033[33mUm exemplo de código com estilo\033[0m')  # Texto cor AMARELO
print('\033[34mUm exemplo de código com estilo\033[0m')  # Texto cor AZUL
print('\033[35mUm exemplo de código com estilo\033[0m')  # Texto cor LILÁS
print('\033[36mUm exemplo de código com estilo\033[0m')  # Texto cor CIANO
print('\033[37mUm exemplo de código com estilo\033[0m')  # Texto cor CINZA
print('\033[38mUm exemplo de código com estilo\033[0m')  # Texto cor BRANCO
