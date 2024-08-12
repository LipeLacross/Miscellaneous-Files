import heapq
from grafo_romenia_com_pesos import RomeniaPonderado

class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph  # grafo com as cidades e distâncias

    def uniform_cost_search(self, start, goal):
        priority_queue = [(0, start)]  # fila de prioridade com custo inicial 0
        visited = set()  # conjunto de cidades já visitadas
        costs = {start: 0}  # dicionário para armazenar o custo mínimo para cada cidade

        while priority_queue:
            current_cost, current_city = heapq.heappop(priority_queue)

            # Se a cidade atual é o destino, retorna o custo total
            if current_city == goal:
                return current_cost

            # Marca a cidade atual como visitada
            visited.add(current_city)

            # Para cada cidade vizinha da cidade atual
            for neighbor in self.graph.G.neighbors(current_city):
                edge_weight = self.graph.G[current_city][neighbor]['weight']
                new_cost = current_cost + edge_weight

                # Se o vizinho não foi visitado ou encontramos um caminho mais barato
                if neighbor not in visited and (neighbor not in costs or new_cost < costs[neighbor]):
                    costs[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))

        # Retorna None se não encontrar o caminho
        return None

if __name__ == "__main__":
    romania = RomeniaPonderado()
    ucs = UniformCostSearch(romania)

    start_city = "Arad"
    goal_city = "Bucharest"
    result = ucs.uniform_cost_search(start_city, goal_city)
    print(f"UCS: O caminho mais curto de {start_city} para {goal_city} tem o custo de {result} km.")
