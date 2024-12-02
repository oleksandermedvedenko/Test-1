def read_matrix():
    # Read dimensions
    M, N = map(int, input().split())
    
    # Read matrix rows
    matrix = []
    for _ in range(M):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    return matrix

def num_islands(grid):
    if not grid:
        return 0
    
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0  # Mark as visited
        dfs(i + 1, j)   # Check down
        dfs(i - 1, j)   # Check up
        dfs(i, j + 1)   # Check right
        dfs(i, j - 1)   # Check left

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
    return count

# Main execution
if __name__ == "__main__":
    matrix = read_matrix()
    result = num_islands(matrix)
    print(result)