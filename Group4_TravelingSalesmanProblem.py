import itertools

def tsp(n, edges, start_node):
    adj_matrix = [[float('inf')] * n for _ in range(n)]
    edge_map = {}  
    
    for edge in edges:
        name, u, v, cost = edge
        u -= 1  
        v -= 1
        adj_matrix[u][v] = cost
        adj_matrix[v][u] = cost 
        edge_map[(u, v)] = name
        edge_map[(v, u)] = name 

    start_node -= 1  

    nodes = [i for i in range(n) if i != start_node]
    min_cost = float('inf')
    best_route = None
    best_edges = None

    for perm in itertools.permutations(nodes):
        current_cost = 0
        current_route = [start_node] + list(perm) + [start_node]
        current_edges = []

        for i in range(len(current_route) - 1):
            u, v = current_route[i], current_route[i + 1]
            current_cost += adj_matrix[u][v]
            current_edges.append(edge_map[(u, v)])

        if current_cost < min_cost:
            min_cost = current_cost
            best_route = current_route
            best_edges = current_edges

    best_route = [node + 1 for node in best_route]

    return min_cost, best_route, best_edges


n = int(input("Enter the number of nodes: "))
e = int(input("Enter the number of edges: "))

edges = []
print("Enter the edges in the format 'edge_number node1 node2 cost':")
for i in range(e):
    edge_data = list(map(int, input().split()))
    edges.append(tuple(edge_data))

start_node = int(input("Enter the starting node: "))

cost, nodes_visited, edges_passed = tsp(n, edges, start_node)

print(f"Cost: {cost}")
print(f"Nodes visited: {' -> '.join(map(str, nodes_visited))}")
print(f"Edges passed: {' -> '.join(map(str, edges_passed))}")