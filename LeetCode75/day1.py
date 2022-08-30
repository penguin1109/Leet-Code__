## Day1: Implementation & Simulation


class Solution:
    def isHappy(self, n):
        seen = set() ## 모든 digit의 제곱의 합을 계산한 수를 저장하기 위해서 사용함
        while True:
            seen.add(n)
            nums = [];length = len(str(n))
            for i in range(length-1, -1, -1):
                nums.append(n // (10 ** i))
                n = n % (10 ** i)
            added = sum(int(i) ** 2 for i in nums)
            if added == 1:
                return True
            else:
                if added in seen:
                    return False
                n = added

    def spiralOrder(self, matrix):
        ## 입력으로 주어지는 matrix는 배열의 형태임
        """ right -> down -> left -> up
        |------->|
        |        |
        |<-------|
        """
        row, col = len(matrix), len(matrix[0])
        check = [[0] * col for _ in range(row)]
        answer = []
        right_end, left_end = col-1, 0
        top_end, bot_end = 0, row-1
        up, down, left, right = False, False, False, True ## 현재 어느 방향으로 이동해야 하는지 나타낸다.
        while left_end <= right_end and top_end <= bot_end:
            if up:
                for i in range(bot_end, top_end - 1, -1):
                    answer.append(matrix[i][left_end])
                    up, down, left, right = False, False, False, True
                left_end += 1
            elif down:
                for i in range(top_end, bot_end + 1):
                    answer.append(matrix[i][right_end])
                    up, down, left, right = False, False, True, False
                right_end -= 1
            elif left:
                for i in range(right_end, left_end-1, -1):
                    answer.append(matrix[bot_end][i])
                    up, down, left, right = True, False, False, False
                bot_end -= 1
            else:
                for i in range(left_end, right_end + 1):
                    answer.append(matrix[top_end][i])
                    up, down, left, right = False, True, False, False
                top_end += 1
        return answer

                
    def findBall(self, grid):
        """
        input: grid (각각의 배열이 어떤 경로를 제공하는지 알려준다.)
        output: 각각의 공이 어떤 위치에 들어가는지, 혹은 들어가지 못하고 막힌다면 -1로 표현하도록 한다.
        - grid에서의 값이 1이면 왼-오
        - grid에서의 값이 -1이면 오-왼
        """
        row, col = len(grid), len(grid[0])
        check = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                left = max(0, j-1)
                right = min(col-1, j+1)
                if grid[i][j] == 1 and grid[i][right] == -1:
                    check[i][j] = -1
                if grid[i][j] == 1 and j == col-1:
                    check[i][j] = -1
                if grid[i][j] == -1 and grid[i][left] == 1:
                    check[i][j] = -1
                if grid[i][j] == -1 and j == 0:
                    check[i][j] = -1
        answer = []
        for ball in range(col):
            temp = ball
            height = 0
            while (height < row):
                if grid[height][temp] == 1 and check[height][temp] == 0:
                    temp = temp + 1
                elif grid[height][temp] == -1 and check[height][temp] == 0:
                    temp = temp - 1
                else:
                    break
                height += 1
            
            if height == row:
                answer.append(temp)
            else:
                answer.append(-1)
        return answer
        




        


if __name__ == "__main__":
    sol = Solution()
    print(sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))

