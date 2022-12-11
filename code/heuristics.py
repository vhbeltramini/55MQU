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
    distancias = [[],[],[]]
    percorridos = [[1],[1],[1]]
    menor = 0
    concluido = False
    menorCidade = 0
    menorcaixeiro = 0

    for i in range(Ncidade):
        vertices_Faltantes.append(i + 1)
    del(vertices_Faltantes[0])

    #print(vertices_Faltantes)

    while concluido == False:
        
        distancias = [[],[],[]]
        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes) - 1):
            for j in range(caixeiros):
                distancias[j].append(distancesMatrix[(percorridos[j][-1],vertices_Faltantes[i])])

        print("Distancias ==")
        print(distancias)
        # Soma as distâncias e acha a menor distância
        somadis = []
        for i in range(len(vertices_Faltantes) - 1):
            linha = []
            soma = 0
            for j in range(caixeiros):
                linha.append(distancias[j][i])
                soma += distancias[j][i]
            somadis.append(linha)
            
            if i == 0:
                menor = soma
                menorCidade = 0
            elif soma < menor:
                menor = soma
                menorCidade = i

        #print(menorCidade)
        print("soma Dis ==")
        print(somadis)
        print(menor)
        for j in range(caixeiros):
            if j == 0:
                menorcaixeiro = 0
            elif somadis[menorCidade][j] < somadis[menorCidade][menorcaixeiro]:
                menorcaixeiro = j

        verticemenor = vertices_Faltantes[menorCidade]
        percorridos[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)
        #print(menorCidade)
        #print(vertices_Faltantes)

        if len(vertices_Faltantes) == 0:
            concluido = True

    ShowResult(vertices_Faltantes, vertices_percoridos, percorridos)


def ShowResult(vertices_Faltantes, vertices_percoridos, percorridos):
    print()
    print(vertices_Faltantes)
    print()
    print(vertices_percoridos)
    print()
    print(percorridos)