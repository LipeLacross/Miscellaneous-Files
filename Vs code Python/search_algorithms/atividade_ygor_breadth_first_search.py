from collections import deque
from grafo_romenia_com_pesos import RomeniaPonderado

class BFS:
    def __init__(self, graph):
        self.graph = graph  # grafo com as cidades e distâncias

    def bfs_search(self, start, goal):
        queue = deque([(start, 0)])  # fila para a busca, contendo o nó e o custo
        visited = set()  # conjunto de cidades já visitadas

        while queue:
            current_city, current_cost = queue.popleft()

            # Se a cidade atual é o destino, retorna o custo total
            if current_city == goal:
                return current_cost

            # Marca a cidade atual como visitada
            visited.add(current_city)

            # Para cada cidade vizinha da cidade atual
            for neighbor in self.graph.G.neighbors(current_city):
                if neighbor not in visited:
                    # Adiciona a cidade vizinha na fila
                    queue.append((neighbor, current_cost + self.graph.G[current_city][neighbor]['weight']))

        # Retorna None se não encontrar o caminho
        return None

if __name__ == "__main__":
    romania = RomeniaPonderado()
    bfs = BFS(romania)

    start_city = "Arad"
    goal_city = "Bucharest"
    result = bfs.bfs_search(start_city, goal_city)
    print(f"BFS: O caminho mais curto de {start_city} para {goal_city} tem o custo de {result} km.")
