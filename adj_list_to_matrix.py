def adjacency_list_to_matrix(adj_list=None):
    """
    Converts a graph from adjacency list representation to an adjacency matrix.

    Parameters:
    adj_list: dict, optional
        An adjacency list representing the graph. 
        Each key is a node, and its value is a list of neighbor nodes.
        Example: {0: [1, 2], 1: [0, 2], 2: [0]}
        If no adjacency list is provided, a default example graph is used.

    Returns:
    adj_matrix: list of lists
        An adjacency matrix where adj_matrix[i][j] = 1 if there is an edge 
        from node i to node j, otherwise 0.
    """

    # DEFAULT GRAPH IF NO INPUT PROVIDED 
    if adj_list is None:
        adj_list = {
            0: [1, 2],
            1: [0, 2],
            2: [0]
        }
        print("No adjacency list provided, using default graph:", adj_list)

    # Number of nodes in the graph
    n = len(adj_list)

    # Initialize n x n adjacency matrix with 0
    # adj_matrix[i][j] will be 1 if there is an edge from i to j
    adj_matrix = [[0] * n for _ in range(n)]

    # Convert adjacency list to adjacency matrix
    for node in adj_list:
        for neighbor in adj_list[node]:
            adj_matrix[node][neighbor] = 1  # 1 indicates an edge exists

    # Print all rows of the adjacency matrix
    print("\nAdjacency Matrix:")
    for row in adj_matrix:
        print(row)

    return adj_matrix


# USER INPUT SECTION
use_input = input("Do you want to enter your own adjacency list? (y/n): ").lower()

if use_input == 'y':
    n = int(input("Enter number of nodes: "))
    adj_list = {}
    print("Enter adjacency list for each node (neighbors separated by space):")
    for i in range(n):
        neighbors = input(f"Neighbors of node {i}: ").strip()
        if neighbors:  # convert to list of integers
            adj_list[i] = list(map(int, neighbors.split()))
        else:
            adj_list[i] = []
    adjacency_list_to_matrix(adj_list)
else:
    # Use default adjacency list
    adjacency_list_to_matrix()