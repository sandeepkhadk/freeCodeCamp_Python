def dfs(adj_matrix, start_node):
    n = len(adj_matrix)     # total number of nodes
    visited = []            # list to store visited nodes
    stack = [start_node]    # stack for DFS

    while stack:
        node = stack.pop()  # remove last element (LIFO)

        if node not in visited:
            visited.append(node)

            # push neighbors into stack
            for neighbor in range(n-1, -1, -1):
                if adj_matrix[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited

# Default Example
default_graph = [
    [0,1,1,0,0],
    [1,0,1,1,0],
    [1,1,0,0,0],
    [0,1,0,0,1],
    [0,0,0,1,0]
]

print("Default Adjacency Matrix:")
for row in default_graph:
    print(row)

print(f"DFS Traversal from node 0: {dfs(default_graph, 0)}")

# User Input Session

print("\n--- User Input Section ---")

n = int(input("Enter number of nodes: "))

print("Enter adjacency matrix row by row:")
adj_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

start = int(input("Enter starting node (0 to n-1): "))

result = dfs(adj_matrix, start)

print(f"Nodes reachable using DFS:{result}")