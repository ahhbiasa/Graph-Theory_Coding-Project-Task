from collections import defaultdict
import heapq

class Graph:
    def __init__(self, n):
        self.adj = defaultdict(list)
        self.nodes = n

    def add_edge(self, name, u, v, cost):
        self.adj[u].append((v, cost, name))
        self.adj[v].append((u, cost, name))

def dijkstra(graph, start):
    distances = {i: float('inf') for i in range(1, graph.nodes + 1)}
    distances[start] = 0
    pq = [(0, start)]
    parent = {start: None}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight, edge_name in graph.adj[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = (current_node, edge_name)
                heapq.heappush(pq, (distance, neighbor))

    return distances, parent

def find_eulerian_path(graph):
    edges = []
    for u in graph.adj:
        for v, cost, name in graph.adj[u]:
            edges.append((u, v, cost, name))

    degree = defaultdict(int)
    for u, v, cost, name in edges:
        degree[u] += 1
        degree[v] += 1

    odd_vertices = [v for v in degree if degree[v] % 2 != 0]

    if len(odd_vertices) > 0:
        shortest_paths = {}
        for i in range(len(odd_vertices)):
            for j in range(i + 1, len(odd_vertices)):
                u = odd_vertices[i]
                v = odd_vertices[j]
                distances, parent = dijkstra(graph, u)
                path = []
                while v is not None:
                    if parent[v]:
                        path.append((parent[v][0], v, parent[v][1]))
                    v = parent[v][0] if parent[v] else None
                path.reverse()
                cost = sum(edge[2] for edge in path)
                shortest_paths[(u, odd_vertices[j])] = (cost, path)

        min_cost_pair = min(shortest_paths.items(), key=lambda x: x[1][0])
        extra_path_cost, extra_path = min_cost_pair[1]
        edges += extra_path

    return edges

def main():
    n = int(input("Nodes: "))
    e = int(input("Edges: "))
    
    graph = Graph(n)

    for i in range(e):
        edge_info = input(str(i) + " Edge info: ")
        edge_info = edge_info.split(" ")
        edge_name = edge_info[0]
        u = int(edge_info[1])
        v = int(edge_info[2])
        cost = int(edge_info[3])
        graph.add_edge(edge_name, u, v, cost)

    start_node = int(input("Start at: "))
    
    edges_traversed = find_eulerian_path(graph)

    total_cost = sum(edge[2] for edge in edges_traversed)
    output_edges = [edge[3] for edge in edges_traversed]

    print(f"Total cost: {total_cost}")
    print("Edges traversed:", " -> ".join(output_edges))

if __name__ == "__main__":
    main()
