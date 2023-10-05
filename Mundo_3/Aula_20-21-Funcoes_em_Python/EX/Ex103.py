def ficha(nome="Undefined", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


nome = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))
if nome.strip() == "" and gols.strip() == '':
    ficha()
elif nome.strip() == "":
    ficha(gols=gols)
elif gols.strip() == '':
    ficha(nome=nome)
else:
    ficha(nome, gols)

