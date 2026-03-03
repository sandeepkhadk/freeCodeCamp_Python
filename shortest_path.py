# Representation of infinity for no connection
INF = float('inf')

# Shortest Path Finder using Dijkstra's Algorithm
def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)
    distances = [INF] * n
    distances[start_node] = 0
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n

    for _ in range(n):
        min_distance = INF
        current = -1

        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        if current == -1:
            break

        visited[current] = True

        for node_no in range(n):
            distance = matrix[current][node_no]

            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance

                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    targets = [target_node] if target_node is not None else range(n)

    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue

        path = ' -> '.join(map(str, paths[node_no]))
        print(f'\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}')

    return distances, paths

# for manual checking

adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

shortest_path(adj_matrix,0,5)

# USER INPUT SECTION 

n = int(input("Enter number of nodes: "))

adj_matrix = []

print("Enter the adjacency matrix row by row.")
print("Use -1 for no connection (it will be treated as INF).")

for i in range(n):
    row = list(map(int, input(f"Row {i}: ").split()))
    
    # Convert -1 to INF
    row = [INF if x == -1 else x for x in row]
    
    adj_matrix.append(row)

start = int(input("Enter start node: "))
target_input = input("Enter target node (or press Enter for all): ")

target = int(target_input) if target_input else None

shortest_path(adj_matrix, start, target)