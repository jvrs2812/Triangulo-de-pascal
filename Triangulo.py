quantidade = int(input("Quantas linhas :"))

def Triangulo(linhas):
    linha = [1]
    zero = [0]

    for i in range(linhas):
        print(linha)

        linha = [i + d for i, d in zip(linha + zero, zero + linha)]
Triangulo(quantidade)
