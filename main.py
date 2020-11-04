class Graph:
    def __init__(self):
        self.graph = {}

    def buildGraph(self, listaAuxCaminhos, verticeSet):
        for v in verticeSet:
            self.graph[v] = {}
        for c in range(len(listaAuxCaminhos)):
            self.graph[listaAuxCaminhos[0][0]][listaAuxCaminhos[0][1]] = (float(listaAuxCaminhos[0][2]), listaAuxCaminhos[0][3])
            self.graph[listaAuxCaminhos[0][1]][listaAuxCaminhos[0][0]] = (float(listaAuxCaminhos[0][2]), listaAuxCaminhos[0][3])
            listaAuxCaminhos.remove(listaAuxCaminhos[0])

    def dijkstra(self, inicial, final):
        verticesNaoVisitadas = self.graph
        menorDistancia = {}
        caminho = [] 
        antecessor = {}

        for vertices in verticesNaoVisitadas:
            menorDistancia[vertices] = float("inf")

        menorDistancia[inicial] = 0

        while(verticesNaoVisitadas):

            menorVertice = None

            for verticeAtual in verticesNaoVisitadas: 
                if menorVertice == None:
                    menorVertice = verticeAtual
                elif menorDistancia[menorVertice] > menorDistancia[verticeAtual]:
                    menorVertice = verticeAtual

            for adjacente, (peso, rua) in verticesNaoVisitadas[menorVertice].items():
                if peso + menorDistancia[menorVertice] < menorDistancia[adjacente]:
                    menorDistancia[adjacente] = peso + menorDistancia[menorVertice]
                    antecessor[adjacente] = (menorVertice, rua)

            verticesNaoVisitadas.pop(menorVertice)

        verticeFinal = final

        while verticeFinal != inicial:
            try:
                caminho.insert(0, verticeFinal)
                verticeFinal = antecessor[verticeFinal][0]

            except Exception:
                return print("inf")

        caminho.insert(0,inicial)

        if menorDistancia[final] != float("inf"):
<<<<<<< HEAD
            return print("Chegou ao destino pela", antecessor[final][1], "com distância de", str(menorDistancia[final]), "metros")

def lerArquivo():
    lista = []
    arq = open("base_de_dados_avalon.txt", "r")
=======
            return print("Chegou ao destino pela", antecessor[final][1], "com distância de:", str(menorDistancia[final]), "metros.")

def lerArquivo():
    lista = []
    arq = open("base_de_dados.txt", "r")
>>>>>>> 3b094ab57f2bcf83c9f3716f0c3317ca81378ba4
    linhas = arq.readlines()
    arq.close()
    for linha in linhas:
        listaCaminhos = linha.split(",")
        cruzamentoInicial = listaCaminhos[0]
        cruzamentoFinal = listaCaminhos[1]
        dist = listaCaminhos[6]
        rua = listaCaminhos[5]
        lista.append(cruzamentoInicial + ", " + cruzamentoFinal + ", " + dist + ", " + rua)
    return lista


verticeSet = set()
verticeSetAux = set()
grafo = Graph()
listaAuxCaminhos = []
caminho = lerArquivo()
pontoPartida = input("Digite o ponto de partida: ")
pontoChegada = input("Digite o ponto de chegada: ")
if pontoPartida == pontoChegada:
    print("Você continuou no mesmo cruzamento, distância: 0")
else:
    for entrada in caminho:
        listaCaminho = entrada.split(", ")

        if ((listaCaminho[0], listaCaminho[1]) in verticeSetAux) or ((listaCaminho[1], listaCaminho[0]) in verticeSetAux):
            for aresta in listaAuxCaminhos:
                if ((aresta[0] == listaCaminho[0]) or (aresta[0] == listaCaminho[1])) and ((aresta[1] == listaCaminho[1]) or (aresta[1] == listaCaminho[0])):
                    if aresta[2] > listaCaminho[2]:
                        listaAuxCaminhos.remove(aresta)
                        listaAuxCaminhos.append(listaCaminho)
        else:
            listaAuxCaminhos.append(listaCaminho)
            verticeSet.add(listaCaminho[0])
            verticeSet.add(listaCaminho[1])
            verticeSetAux.add((listaCaminho[0], listaCaminho[1]))

    if (pontoPartida not in verticeSet) or (pontoChegada not in verticeSet):
        print("inf")
    else:
        grafo.buildGraph(listaAuxCaminhos, verticeSet)
        grafo.dijkstra(pontoPartida, pontoChegada)
