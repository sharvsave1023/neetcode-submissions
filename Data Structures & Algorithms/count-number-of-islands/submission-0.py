from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1, 0), (-1,0)]

        def bfs(r, c, grid, visited): 

            queue = deque([(r,c)])
            visited.add((r,c))

            while queue: 

                r, c = queue.popleft()

                for dr, dc in directions: 

                    if 0 <=  r + dr < m and 0 <= c + dc < n and grid[r + dr][c + dc] == "1" and (r + dr, c + dc) not in visited:
                        visited.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc)) 

            return 1

        visited = set()
        res = 0
        for r in range(m): 
            for c in range(n): 
                
                if grid[r][c] == "1" and (r, c) not in visited: 
                    res += bfs(r, c, grid, visited)

        return res




