def dfs_n_queens(n):
    if n < 1:
        return []

    result = []

    # DFS helper function
    def dfs(row, cols):
        if row == n:
            result.append(cols[:])
            return

        for col in range(n):
            valid = True

            for r in range(row):
                # check same column or diagonal conflict
                if cols[r] == col or abs(cols[r] - col) == row - r:
                    valid = False
                    break

            if valid:
                cols.append(col)
                dfs(row + 1, cols)
                cols.pop()  # backtrack

    dfs(0, [])
    return result


# User Input Session
try:
    n = int(input("Enter the number of queens (n): "))
    solutions = dfs_n_queens(n)

    if not solutions:
        print(f"No solutions exist for n = {n}.")
    else:
        print(f"Total solutions for n = {n}: {len(solutions)}")
        for i, sol in enumerate(solutions, 1):
            print(f"Solution {i}: {sol}")

except ValueError:
    print("Please enter a valid integer.")