from queue import PriorityQueue
from grafo_romenia_com_pesos import RomeniaPonderado

class Node:
    def __init__(self, city, cost):
        self.city = city  # cidade de agora
        self.cost = cost  # custo total até chegar nessa cidade

    #comparar nós, baseado no custo
    def __lt__(self, other):
        return self.cost < other.cost

class SearchTree:
    def __init__(self, graph):
        self.graph = graph  #grafo com as cidades e distâncias
        self.frontier = PriorityQueue()  # fronteira usando uma fila de prioridade
        #slide do prof ->fila de prioridade remove primeiro o nó com o menor custo, de acordo com alguma função de avaliação
        
        self.explored = set()  # lista de cidades já exploradas

    def best_first_search(self, start, goal):
        # add a cidade inicial na fronteira com dist 0
        self.frontier.put(Node(start, 0))

        #enquanto tiver nós na fronteira
        while not self.frontier.empty():
            #pega nó com menor custo
            current_node = self.frontier.get()
            current_city = current_node.city

            #se a cidade já foi explorada, vai para a próxima iteração
            if current_city in self.explored:
                continue

            # torna a cidade como explorada
            self.explored.add(current_city)

            # se a cidade atual é destino, retorna o custo total
            if current_city == goal:
                return current_node.cost

            # pra cada cidade vizinha da cidade atual
            for neighbor in self.graph.G.neighbors(current_city):
                # Se cidade vizinha ainda não foi explorada
                if neighbor not in self.explored:
                    # calc o cust total para chegar a cidade vizinha
                    edge_weight = self.graph.G[current_city][neighbor]['weight']
                    total_cost = current_node.cost + edge_weight
                    # add cidade vizinha na fronteira
                    self.frontier.put(Node(neighbor, total_cost))

        # None se não achar nada
        return None

if __name__ == "__main__":
    romania = RomeniaPonderado()
    #tree com grafo
    search_tree = SearchTree(romania)

    start_city = "Arad"
    goal_city = "Bucharest"
    result = search_tree.best_first_search(start_city, goal_city)
    print(f"O caminho mais curto de {start_city} para {goal_city} tem o custo de {result} km.")
