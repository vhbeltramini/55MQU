# Gerar Heurística para o problema do Múltiplo caixeiro viajante
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''

print("Start")

def Heurisitica1(matriz, Ncidade):
    distancesMatrix = matriz
    caixeiros = 3
    vertices_Faltantes = []
    vertices_percoridos = [1]
    distancias = [[]]
    somadis = []
    menor = 0
    concluido = False
    menorCidade = 0

    for i in range(Ncidade):
        vertices_Faltantes.append(i + 1)

    while concluido == False:

        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes) - 1):
            for j in range(caixeiros):
                distancias[j].append(distancesMatrix[j[-1]][vertices_Faltantes[i]])

        # Soma as distâncias e acha a menor distância
        for i in range(len(vertices_Faltantes) - 1):
            linha = [[]]
            soma = 0
            for j in range(caixeiros):
                linha[i].append(distancias[j][i])
                soma += distancias[j][i]
                print("Linha == ")
                print(linha)
                somadis[j].append(linha)

            if i == 0:
                menor = soma
                menorCidade = i
            elif soma < menor:
                menor = soma
                menorCidade = i

        for i in range(caixeiros):
            for j in range(caixeiros):
                if (somadis[menorCidade][i] + somadis[menorCidade][j]) == menor:
                    print(somadis[menorCidade][i] + somadis[menorCidade][j])
                    verticemenor = vertices_Faltantes[menorCidade]

                    if somadis[menorCidade][i] < somadis[menorCidade][j]:
                        distancias[i].append(verticemenor)
                    elif somadis[menorCidade][i] > somadis[menorCidade][j]:
                        distancias[j].append(verticemenor)

                    del (vertices_Faltantes[menorCidade])
                    vertices_percoridos.append(verticemenor)
                    print(vertices_Faltantes)

        if len(vertices_Faltantes) == 0:
            concluido = True

        for j in range(caixeiros):
            distancias[j].append(0)

    ShowResult(vertices_Faltantes, vertices_percoridos)


def ShowResult(vertices_Faltantes, vertices_percoridos):
    print()
    print(vertices_Faltantes)
    print()
    print(vertices_percoridos)
