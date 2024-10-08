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
`itertools`: This module provides functions that help with efficient looping. In this case, we use `itertools.permutations()` to generate all possible orderings of nodes for checking all possible paths in the TSP.

### 1.1.2 TSP Function Definition
``` py
def tsp(n, edges, start_node):
```
This function takes the number of nodes, the list of edges, and the starting node as input.
- `n`: The number of nodes in the graph.
- `edges`: A list of tuples, where each tuple represents an edge between two nodes with a cost (e.g., `(edge_number, node1, node2, cost)`).
- `start_node`: The node from which the TSP journey starts and ends.

### 1.1.3 Adjacency Matrix and Edge Map
```py
    adj_matrix = [[float('inf')] * n for _ in range(n)]
    edge_map = {}
```
- `adj_matrix`: A 2D list representing the cost to travel between any two nodes. Initially, all distances are set to infinity (`float('inf')`) because no edges have been defined yet. The matrix will eventually hold the travel costs between nodes.
- `edge_map`: A dictionary that maps pairs of nodes to the name of the edge between them. This helps retrieve which edges are used in the best route.

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
This loop processes the `edges` list. Each edge has:
- `name`: Identifier of the edge (e.g., edge number).
- `u, v`: Nodes connected by the edge. Subtracting 1 (`u -= 1`) adjusts the input to 0-based indexing (since Python lists are indexed from 0).
- `cost`: The travel cost between nodes `u` and `v`.

The adjacency matrix is filled such that the travel cost between node `u` and node `v` is recorded in both directions (since the graph is assumed to be undirected).
The `edge_map` dictionary stores the name of each edge between two nodes.

### 1.1.5 Adjusting the Starting Node
```py
    start_node -= 1
```
The `start_node` input is adjusted to 0-based indexing.

### 1.1.6 Generating Permutations of Nodes
```py
    nodes = [i for i in range(n) if i != start_node]
    min_cost = float('inf')
    best_route = None
    best_edges = None
```
- `nodes`: This creates a list of all nodes except the `start_node`. These are the nodes that need to be visited during the TSP.
- `min_cost`: This variable holds the minimum cost found during the search. It is initially set to infinity.
- `best_route`: Will store the best route (order of nodes) found.
- `best_edges`: Will store the edges used in the best route.

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
**1st For Loop**
- `itertools.permutations(nodes)`: This generates all possible orderings (permutations) of the `nodes` list. The TSP must try all possible routes to find the shortest.
- `current_route`: The current route starts at the `start_node`, visits each node in the current permutation `perm`, and then returns to the `start_node`.
- `current_cost`: Tracks the total travel cost of the current route.
- `current_edges`: Tracks the edges used in the current route.

**2nd For Loop**
This loop iterates through pairs of consecutive nodes in the current route and accumulates the travel cost from `adj_matrix[u][v]`. It also records the corresponding edge names from `edge_map`.

**If-Case**
If the current route has a lower cost than the previously found routes, it becomes the new best route. The `min_cost`, `best_route`, and `best_edges` are updated accordingly.

### 1.1.8 Adjusting the Best Route for Output
```py
    best_route = [node + 1 for node in best_route]
```
Since we used 0-based indexing internally, this converts the `best_route` back to 1-based indexing to match user expectations

### 1.1.9 Returning the Result
```py
    return min_cost, best_route, best_edges
```
Returns the:
- `min_cost`: The minimum cost of the best route.
- `best_route`: The order of nodes in the best route.
- `best_edges`: The edges traversed in the best route.

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

Imagine we were visiting a city, and you want to visit every street in this city once in the most minimum possible distance to accomplish this tour. This is essentially what the Chinese Postman Problem is about.

We can think of these streets as the edges, connecting vertices (intersections). We would need to have these vertices at an even number, because then we could traverse each edge exactly once.

We can represent our graph as an adjacency list using a dictionary of dictionaries. Each edge is stored with its cost and name.

```python
graph = defaultdict(dict)
edge_map = {}

for edge in edges:
    name, u, v, cost = edge
    u -= 1
    v -= 1
    graph[u][v] = (cost, name)
    graph[v][u] = (cost, name)
    edge_map[(u, v)] = edge_map[(v, u)] = name
```

We will have to check if this graph has a eularian circuit. If all vertices have even degree, then such a circuit exists, and we can solve the problem directly.

```python
def find_odd_degree_vertices():
    return [v for v in range(n) if len(graph[v]) % 2 != 0]

odd_vertices = find_odd_degree_vertices()
if not odd_vertices:
    # Eulerian circuit exists
```

But if we have odd degree vertices, we need to add extra edges to make all vertices even degree. We do that by finding a minimum weight perfect matching among the odd degree vertices.

```python
for matching in itertools.combinations(range(n_odd), n_odd // 2):
    cost = sum(dist[odd_vertices[i]][odd_vertices[j]] for i, j in zip(matching, set(range(n_odd)) - set(matching)))
    if cost < min_cost:
        min_cost = cost
        best_matching = matching
```

The graph is augmented with the edges from the minimum weight perfect matching. Then we can find for a eularian circuit with this function:

```python
def find_eulerian_circuit(graph, start):
    # pass
```

Then we can construct a final solution by following the circuit, keeping track of the nodes and edges visited, and calculating the cost along the way.

# Knights Tour
The goal of Knights Tour problem is to move a knight in a `NxN` size chessboard to visit all square on the board exactly once, using only knight's legal moves.
## 1.1 Code Explanation (TSP Function):
### 1.1.1 Knight Move
These are the moves in `(X, Y)` format that can be done by a knight on the chessboard.
```
knight_moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]
```
### 1.1.2 Check Valid Move
The `is_valid` function checks if the knight's move is within the chessboard and if the square hasn't been visited yet.
```
def is_valid(x, y, board, N):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1
```
### 1.1.3 Backtracking
`knights_tour` function is to backtrack the knight to move on each squares exactly once. 
```
def knights_tour(board, x, y, move_count, N, moves):
    if move_count == N * N:
        return True
```
the `base` part to check if the knight has visited all square or not.
```
    for move in knight_moves:
        next_x, next_y = x + move[0], y + move[1]
        if is_valid(next_x, next_y, board, N):
            board[next_x][next_y] = move_count
            moves.append((next_x, next_y))
            if knights_tour(board, next_x, next_y, move_count + 1, N, moves):
                return True
            board[next_x][next_y] = -1
            moves.pop()
    return False
```
and this part is to find all possible moves the knight can make by using a loop

### 1.1.4 Starts Knight Tour
`start_knights_tour` function to initialize the cheesboard and start the tour based on the input.
```
def start_knights_tour(N, start_x, start_y):
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[start_x][start_y] = 0
    moves = [(start_x, start_y)]
```
this part to initialize all cells in the chessboard and knights start position.
```
    if knights_tour(board, start_x, start_y, 1, N, moves):
        for move in moves:
            print(f"{move[0]} {move[1]}")
    else:
        print("No solution found")
```
if the tour are completed, it will print all the cells that are visited from the start position.
### 1.1.5 User-Input
The chessboard size `N` and the knight's starting position `(start_x, start_y)` are taken from the user.
```
N = int(input("Enter the size of the chessboard (N x N): "))
start_x, start_y = map(int, input("Enter the starting position of the knight (x y): ").split())
```
