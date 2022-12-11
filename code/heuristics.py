# Gerar Heurística para o problema do Múltiplo caixeiro viajante
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''

print("Start")
C = [] # lista das distânciasß
linha1 = [0,1,1,1,1,1,1] # lista vazia
linha2 = [1,0,1,1,1,1,1] # lista vazia
linha3 = [1,1,0,1,1,1,1] # lista vazia
linha4 = [1,1,1,0,1,1,1] # lista vazia
linha5 = [1,1,1,1,0,1,1] # lista vazia
linha6 = [1,1,1,1,1,0,1] # lista vazia
linha7 = [1,1,1,1,1,1,0] # lista vazia
C.append(linha1)
C.append(linha2)
C.append(linha3)
C.append(linha4)
C.append(linha5)
C.append(linha6)
C.append(linha7)

print(C)

def Heurisitica1(matriz, Ncidade):

    C = matriz
    m = 3
    vertices_Faltantes = []
    vertices_percoridos = [1]
    distancia1 = []
    distancia2 = []
    distancia3 = []
    somadis = []
    menor = 0
    caixieiro1 = [1]
    caixieiro2 = [1]
    caixieiro3 = [1]
    concluido = False


    for i in range(Ncidade):
        vertices_Faltantes.append(i+1)

    while concluido == False:

        #calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes)-1):
            for j in range(m):
                if j == 0:
                    distancia1.append(C[caixieiro1[-1]][vertices_Faltantes[i]])
                elif j == 1:
                    distancia2.append(C[caixieiro2[-1]][vertices_Faltantes[i]])
                else:
                    distancia3.append(C[caixieiro3[-1]][vertices_Faltantes[i]])

        #Soma as distâncias e acha a menor distância

        for i in range(len(vertices_Faltantes)-1):
            linha = distancia1[i], distancia2[i], distancia3[i]
            somadis.append(linha)
            soma = distancia1[i] + distancia2[i] + distancia3[i]
            if i == 0:
                menor = soma
            elif soma < menor:
                menor = soma

        for i in range(len(somadis)-1):
            if (somadis[i][0] + somadis[i][1] + somadis[i][2]) == menor:
                print(somadis[i][0] + somadis[i][1] + somadis[i][2])
                verticemenor = vertices_Faltantes[i]

                if somadis[i][0] < somadis[i][1] and somadis[i][0] < somadis[i][2]:
                    caixieiro1.append(verticemenor)
                elif somadis[i][1] < somadis[i][0] and somadis[i][1] < somadis[i][2]:
                    caixieiro2.append(verticemenor)
                elif somadis[i][2] < somadis[i][0] and somadis[i][2] < somadis[i][1]:
                     caixieiro3.append(verticemenor)

                del(vertices_Faltantes[i])
                vertices_percoridos.append(verticemenor)
                print(vertices_Faltantes)

        if len(vertices_Faltantes) == 0:
            concluido = True
            caixieiro1.append(0)
            caixieiro2.append(0)
            caixieiro3.append(0)

    ShowResult(vertices_Faltantes, vertices_percoridos)

def ShowResult(vertices_Faltantes, vertices_percoridos):
    print()
    print(vertices_Faltantes)
    print()
    print(vertices_percoridos)