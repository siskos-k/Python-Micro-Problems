class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, i, j):
        """
        :type grid: List[List[str]]
        :type i: int
        :type j: int
        :rtype: None
        """
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return

        # Mark the current cell as visited.
        grid[i][j] = '0'

        # Explore the four adjacent cells.
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)



grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

solution = Solution()
print(solution.numIslands(grid))  # Output: 1
