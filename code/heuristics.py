# Gerar Heurística para o problema do Múltiplo caixeiro viajante
'''

restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
  1  2  3  4  5  6  7
1[0][1][1][1][0][0][0]
2[1][0][0][1][0][0][0]
3[1][0][0][1][1][0][1]
4[1][1][1][0][1][0][0]
5[0][0][1][1][0][1][0]
6[0][0][0][0][1][0][1]
7[0][0][1][0][0][1][0]

'''

print("Start")
n_linhas = 7
n_colunas = 7
C = []  # lista das distâncias
m = 2
linha1 = [0, 1, 1, 1, 1, 1, 1]  # lista vazia
linha2 = [1, 0, 1, 1, 1, 1, 1]  # lista vazia
linha3 = [1, 1, 0, 1, 1, 1, 1]  # lista vazia
linha4 = [1, 1, 1, 0, 1, 1, 1]  # lista vazia
linha5 = [1, 1, 1, 1, 0, 1, 1]  # lista vazia
linha6 = [1, 1, 1, 1, 1, 0, 1]  # lista vazia
linha7 = [1, 1, 1, 1, 1, 1, 0]  # lista vazia
C.append(linha1)
C.append(linha2)
C.append(linha3)
C.append(linha4)
C.append(linha5)
C.append(linha6)
C.append(linha7)

X = []  # matriz com as listas de caminhos percorridos para cada caixieiro (m)


def Heurisitica1():
    vertices_Faltantes = [2, 3, 4, 5, 6, 7]
    vertices_percoridos = [1]
    distancia1 = []
    distancia2 = []
    somadis = []
    menor = 0
    caixieiro1 = [1]
    caixieiro2 = [1]
    concluido = False

    while concluido == False:

        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes)-1):
            for j in range(m):
                if j == 0:
                    distancia1.append(C[caixieiro1[-1]][vertices_Faltantes[i]])
                elif j == 1:
                    distancia2.append(C[caixieiro2[-1]][vertices_Faltantes[i]])

        # Soma as distâncias e acha a menor distância
        for i in range(len(vertices_Faltantes)-1):
            for j in range(m):
                if j == 0:
                    somadis[i] = distancia1[i]
                elif j == 1:
                    somadis[i] += distancia2[i]
                if i == 0:
                    menor = somadis[i]
                elif somadis[i] < menor:
                    menor = somadis[i]

        for i in range(somadis):
            if somadis[i] == menor:
                verticemenor = vertices_Faltantes[i]
                for j in range(m):
                    if j == 0:
                        menorcaixieiro = distancia1[i]
                        caixeiro = 1
                    elif j == 1:
                        if distancia2[i] < menorcaixieiro:
                            menorcaixieiro = distancia2[i]
                            caixeiro = 2

                if caixeiro == 1:
                    caixieiro1.append(verticemenor)

                elif caixeiro == 2:
                    caixieiro2.append(verticemenor)

                del (vertices_Faltantes[i])
                vertices_percoridos.append(verticemenor)

        if len(vertices_Faltantes) == 0:
            concluido = True
            caixieiro1.append(0)
            caixieiro2.append(0)

    ShowResult(vertices_Faltantes, vertices_percoridos)


def ShowResult(vertices_Faltantes, vertices_percoridos):
    print(X)
    print()
    print(vertices_Faltantes)
    print()
    print(vertices_percoridos)


Heurisitica1()
