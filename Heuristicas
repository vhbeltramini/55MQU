# Gerar Heurística para o problema do Múltiplo caixeiro viajante

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

G = (V,A)
V = vertices
A = arestas

Cij = matriz com as distâncias
m = quantidade de caixeiros
Xij = matriz para ver os vertices percorridos por cada caixiero (recebe 1 caso tenha passado)

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
C = [] # lista das distâncias
m = 2
linha1 = [0,1,1,1,0,0,0] # lista vazia
linha2 = [1,0,0,1,0,0,0] # lista vazia
linha3 = [1,0,0,1,1,0,1] # lista vazia
linha4 = [1,1,1,0,1,0,0] # lista vazia
linha5 = [0,0,1,1,0,1,0] # lista vazia
linha6 = [0,0,0,0,1,0,1] # lista vazia
linha7 = [0,0,1,0,0,1,0] # lista vazia
C.append(linha1)
C.append(linha2)
C.append(linha3)
C.append(linha4)
C.append(linha5)
C.append(linha6)
C.append(linha7)

X = [] #matriz com as listas de caminhos percorridos para cada caixieiro (m)


def Heurisitica1():
    vertices_Faltantes = [2,3,4,5,6,7]
    vertices_percoridos = [1]
    caixieiro1 = []
    caixieiro2 = []
    
    while len(vertices_Faltantes) > 0:
        verticeAtual = vertices_Faltantes[1]
        del(vertices_Faltantes[0])
        posicao += 1
        
        for i in range(m):
            caminhos_possiveis = []
            for j in range(n_linhas):
                if C[vertices_Faltantes[posicao]][j] > 0:
                    caminhos_possiveis.append(j+1)
            # ordenar caminhos_possiveis pela distância para solução gulosa
            for j in range(vertices_Faltantes):
                if caminhos_possiveis[j] == vertices_Faltantes[j]:
                    if i == 0:
                        caixieiro1.append(vertices_Faltantes[j])
                        vertices_percoridos.append(vertices_Faltantes[j])
                        del(vertices_Faltantes[j])
                        exit()
                    elif i == 1:
                        caixieiro2.append(vertices_Faltantes[j])
                        vertices_percoridos.append(vertices_Faltantes[j])
                        del(vertices_Faltantes[j])
                        exit()
            
    
    ShowResult


def ShowResult():
    print(X)
    print()
    print(vertices_Faltantes)
    print()
    print(vertices_percoridos)

Heurisitica1