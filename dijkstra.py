import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# Example usage:
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_edge('A', 'B', 6)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 3)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 4)

start_node = 'A'
end_node = 'D'
shortest_distances = dijkstra(graph, start_node)
shortest_distance_to_end_node = shortest_distances[end_node]
print(f"The shortest distance from {start_node} to {end_node} is: {shortest_distance_to_end_node}")
