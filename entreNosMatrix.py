
#!/usr/bin/python3
"""
#25089 Em trenós (ou entre nós?)
Aluno: Jose Ceron Neto 316571 
Disciplina: Projeto e Análise de Algoritmos - PAA - CCO00201_A_2020_2
Prof. Dr. Diego Furtado Silva
Algoritmo Dijkstra-guloso baseado no codigo de Divyanshu Mehta para geeksforgeeks.org
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
"""
  
INT_MAX = 999
import sys
  
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
  
      
    # A utility function to find the vertex with 
    # minimum distance value, from the set of vertices 
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
  
        # Initilaize minimum distance for next node
        min = INT_MAX
        
        # Search not nearest vertex not in the 
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
  
        return min_index
  
    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation
    def dijkstra(self, src, dst):
  
        dist = [INT_MAX] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
  
        for cout in range(self.V):
  
            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
  
            # Put the minimum distance vertex in the 
            # shotest path tree
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
  
        return dist[dst]
  
if __name__ == "__main__":
    try:
        linha1 = input().split()
    except:
        print("ERROR")

    #numero de salas/vertices
    M = int(linha1[0])
    ################################################## VERIFICAR ##############################################
    #M = M+1
    # numero de corredores - arestas
    E = int(linha1[1])
    # numero de tubulacoes - arestas
    N = int(linha1[2])
    # numero de consultas
    C = int(linha1[3])

    #print(linha1)
    #ler linha com as triplas de arestas e pesos entre as salas via corredores
    linha2 = input().split()
    #ler linha com os pares de arestas entre as salas via tubulação de ventilaçao
    linha3 = input().split()

    #ler cada consulta a ser realizada
    consulta = []
    for i in range(C):
        consulta.append(int(input()))
    
    #montar estrutura dos grafos: Grafo Tripulante / Grafo Impostor
    grafoTripulante = Graph(M)
    grafoImpostor = Graph(M)
    
    #Constuir a matriz de adjacencias do grafo Tripulante e grafo Impostor
    # Por se tratar de grado nao direcionado a matriz é simetrica onde grafoX[u][v] = grafoX[v][u]
    for i in range(E):
        grafoTripulante.graph[int(linha2[i*3])][int(linha2[(i*3)+1])] = float(linha2[(i*3)+2])
        grafoTripulante.graph[int(linha2[(i*3)+1])][int(linha2[i*3])] = float(linha2[(i*3)+2])

        grafoImpostor.graph[int(linha2[i*3])][int(linha2[(i*3)+1])] = float(linha2[(i*3)+2])
        grafoImpostor.graph[int(linha2[(i*3)+1])][int(linha2[i*3])] = float(linha2[(i*3)+2])

    #print(grafoTripulante.graph)

    #print(grafoImpostor.graph)

    #Atualização da matriz de adjacencias dop grafo Impostor com as arestas de tubulacao
    #Checando se o corredor entre as salas tem que possuem tubulacao de ventilacao
    # possuem distancia maior que 1.0 - distancia da tubulacao. Em caso afirmativo atualizar
    # o peso na matriz.

    for i in range(N):

        if (grafoImpostor.graph[int(linha3[i*2])][int(linha3[(i*2)+1])] > 1.0 or grafoImpostor.graph[int(linha3[i*2])][int(linha3[(i*2)+1])] == 0):
            grafoImpostor.graph[int(linha3[i*2])][int(linha3[(i*2)+1])] = 1.0
            grafoImpostor.graph[int(linha3[(i*2)+1])][int(linha3[i*2])] = 1.0
        
    
    # Para cada consulta C, realizar o caminho mais curto. Sendo que se o caminho do tripulante 
    # for menor, imprimir 'victory'. Se o do impostor for menor,imprimir 'defeat'
    for i in range(C):
        distTripulante = grafoTripulante.dijkstra(0,int(consulta[i]))
        distImpostor = grafoImpostor.dijkstra(0,int(consulta[i]))
        if(distTripulante<=distImpostor):
            print('victory')
        else:
            print('defeat')



