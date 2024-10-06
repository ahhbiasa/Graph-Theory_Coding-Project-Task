# Graph-Theory_Coding-Project-Task
This is group 4's repo for the coding project task in graph theory. The following will be the code explanations for each question:

<br>

# 1. Traveling Salesman Problem
The goal of the Traveling Salesman Problem (TSP) is to find the shortest possible route that visits a set of nodes (cities) exactly once and returns to the starting node.

<br>

## 1.1 Code Explanation (TSP Function):
### 1.1.1 Importing itertools
```py
import itertools
```
This module is used to generate permutations of nodes, which helps in exploring all possible routes.

### 1.1.2 TSP Function Definition
``` py
def tsp(n, edges, start_node):
```
This function takes the number of nodes, the list of edges, and the starting node as input.

### 1.1.3 Adjacency Matrix and Edge Map
```py
    adj_matrix = [[float('inf')] * n for _ in range(n)]
    edge_map = {}
```
- `adj_matrix`: A 2D list initialized with infinity (`float('inf')`) to represent the cost between nodes. It will be updated with actual edge costs.
- `edge_map`: A dictionary to map edges to their names.

### 1.1.4 Populating the Adjacency Matrix and Edge Map
```py
    for edge in edges:
        name, u, v, cost = edge
        u -= 1  
        v -= 1
        adj_matrix[u][v] = cost
        adj_matrix[v][u] = cost 
        edge_map[(u, v)] = name
        edge_map[(v, u)] = name
```
This loop updates the adjacency matrix with the costs and the edge map with the edge names.

### 1.1.5 Adjusting the Starting Node
```py
    start_node -= 1
```
Adjusts the starting node index to be zero-based.

### 1.1.6 Generating Permutations of Nodes
```py
    nodes = [i for i in range(n) if i != start_node]
    min_cost = float('inf')
    best_route = None
    best_edges = None
```
- `nodes`: A list of nodes excluding the starting node.
- `min_cost`: Initialized to infinity to keep track of the minimum cost found.
- `best_route and best_edges`: To store the best route and corresponding edges.

### 1.1.7 Evaluating All Permutations
```py
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
```
This loop evaluates all possible routes (permutations of nodes) and calculates the cost for each route. If a route has a lower cost than the current minimum, it updates the minimum cost and the best route.

### 1.1.8 Adjusting the Best Route for Output
```py
    best_route = [node + 1 for node in best_route]
```
Converts the zero-based node indices back to one-based for output.

### 1.1.9 Returning the Result
```py
    return min_cost, best_route, best_edges
```
Returns the minimum cost, the best route, and the edges passed.

<br>

## 1.2 Code Explanation (Main):
### 1.2.1 Reading the Number of Nodes and Edges:
```py
n = int(input("Enter the number of nodes: "))
e = int(input("Enter the number of edges: "))
```
- `n`: is the number of nodes in the graph.
- `e`: is the number of edges connecting these nodes.

### 1.2.2 Reading the Edges
```py
edges = []
print("Enter the edges in the format 'edge_number node1 node2 cost':")
for i in range(e):
    edge_data = list(map(int, input().split()))
    edges.append(tuple(edge_data))
```
- An empty list `edges` is initialized to store the edge information.
- The code prompts the user to enter each edge in the format: edge number, node1, node2, and cost.
- For each edge, the input is split into individual integers and converted into a tuple, which is then appended to the `edges` list.

### 1.2.3 Reading the Starting Node
```py
start_node = int(input("Enter the starting node: "))
```
The starting node for the TSP is read from the user.

### 1.2.4 Solving the TSP by Calling the TSP Function
```py
cost, nodes_visited, edges_passed = tsp(n, edges, start_node)
```
- The `tsp` function is called with the number of nodes, the list of edges, and the starting node.
- The function returns three values:
  - `cost`: The minimum cost of the TSP route.
  - `nodes_visited`: The sequence of nodes visited in the optimal route.
  - `edges_passed`: The sequence of edges used in the optimal route.

### 1.2.5 Printing the Results:
```py
print(f"Cost: {cost}")
print(f"Nodes visited: {' -> '.join(map(str, nodes_visited))}")
print(f"Edges passed: {' -> '.join(map(str, edges_passed))}")
```
- The minimum cost of the TSP route is printed.
- The sequence of nodes visited is printed in a readable format, with nodes separated by " -> ".
- The sequence of edges used is printed in a similar format.

<br>

## 1.3 Logical Explanation
The code solves the Traveling Salesman Problem (TSP) using a brute-force approach by evaluating all possible routes (permutations) and selecting the one with the minimum cost.

### 1.3.1 Initialization
- **Adjacency Matrix**: A 2D list (`adj_matrix`) is created to store the cost between each pair of nodes. Initially, all values are set to infinity (`float('inf')`) to indicate no direct path.
- **Edge Map**: A dictionary (`edge_map`) is used to map each edge to its name for easy reference.

### 1.3.2 Input Parsing
The code reads the number of nodes (`n`) and edges (`e`). For each edge, it reads the edge name, the two nodes it connects, and the cost. It then updates the adjacency matrix with the cost and the edge map with the edge name.

### 1.3.3 Adjusting Indices
The node indices are adjusted to be zero-based (subtracting 1) for easier array indexing.

### 1.3.4 Generating Permutations
A list of nodes excluding the starting node is created. With the use of `itertools.permutations`, the code can generate all possible permutations of these nodes. Each permutation represents a possible route.

### 1.3.5 Evaluating Routes
For each permutation, the code constructs a route that starts and ends at the starting node. It calculates the total cost of the route by summing the costs of the edges in the route. It also keeps track of the edges used in the route.

### 1.3.6 Finding the Minimum Cost Route:
The code compares the cost of each route with the current minimum cost. If a route has a lower cost, it updates the minimum cost and stores the route and edges as the best route.

### 1.3.7 Adjusting Output
The best route is converted back to one-based indexing for output.

### 1.3.8 Returning the Result
The function returns the minimum cost, the best route, and the edges used in that route.

<br>

# Chinese Postman Problem

# Knights Tour
