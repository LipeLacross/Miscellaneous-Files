from collections import deque
from grafo_romenia_com_pesos import RomeniaPonderado

class BidirectionalSearch:
    def __init__(self, graph):
        self.graph = graph  # grafo com as cidades e distâncias

    def bidirectional_search(self, start, goal):
        if start == goal:
            return 0

        # Fila para a busca a partir do início
        queue_start = deque([(start, 0)])
        visited_start = {start: 0}

        # Fila para a busca a partir do objetivo
        queue_goal = deque([(goal, 0)])
        visited_goal = {goal: 0}

        while queue_start and queue_goal:
            # Expande a busca a partir do início
            current_city_start, current_cost_start = queue_start.popleft()
            for neighbor in self.graph.G.neighbors(current_city_start):
                new_cost = current_cost_start + self.graph.G[current_city_start][neighbor]['weight']
                if neighbor in visited_goal:
                    return new_cost + visited_goal[neighbor]
                if neighbor not in visited_start:
                    visited_start[neighbor] = new_cost
                    queue_start.append((neighbor, new_cost))

            # Expande a busca a partir do objetivo
            current_city_goal, current_cost_goal = queue_goal.popleft()
            for neighbor in self.graph.G.neighbors(current_city_goal):
                new_cost = current_cost_goal + self.graph.G[current_city_goal][neighbor]['weight']
                if neighbor in visited_start:
                    return new_cost + visited_start[neighbor]
                if neighbor not in visited_goal:
                    visited_goal[neighbor] = new_cost
                    queue_goal.append((neighbor, new_cost))

        # Retorna None se não encontrar o caminho
        return None

if __name__ == "__main__":
    romania = RomeniaPonderado()
    bidirectional = BidirectionalSearch(romania)

    start_city = "Arad"
    goal_city = "Bucharest"
    result = bidirectional.bidirectional_search(start_city, goal_city)
    print(f"Busca Bidirecional: O caminho mais curto de {start_city} para {goal_city} tem o custo de {result} km.")
