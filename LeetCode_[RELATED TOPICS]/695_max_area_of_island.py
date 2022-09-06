## 695. Max Area of Island ##

"""
- mxn 크기의 0과 1로 이루어진 grid matrix가 주어지며, island라고 하면 1로만 이루어져 있다. 
- 제일 큰 영역의 island의 넓이를 구하고, 없다면 0을 반환한다.
- 상당히 전형적인 BFS(breath first search) 문제이다.
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        row, col = len(grid), len(grid[0])
        answer = 0
        check = [[0] * col for _ in range(row)]
        def dfs(x, y):
            dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
            stack = [(x,y)]
            cnt = 0
            while stack:
                a,b = stack.pop()
                check[a][b] = 1
                cnt += 1
                for d in range(4):
                    nx,ny = a + dx[d], b + dy[d]
                    if (0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1 and check[nx][ny] == 0):
                        check[nx][ny] = 1 ## 여기서 이 부분을 추가해 주지 않으면 반복해서 탐색하게 되는 경우가 생긴다.
                        stack.append((nx, ny))
            return cnt
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and check[r][c] == 0:
                    answer = max(answer, dfs(r,c))
        return answer
        


