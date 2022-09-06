## GREEDY ##
from collections import defaultdict
class Solution:
    def longestPalindrome(self, words):
        """
        - 이 문제를 푸는데 꽤나 애를 많이 먹었는데, 중요한 것은 스스로가 palindrome인 아이들의 개수의 홀수/짝수 여부였다.
        - 그럼에도 불구하고 마지막에 반복되는 word에 대한 탐색을 줄이기 위해서 list(set(words))를 사용하니 TLE는 해결이 되었다.
        """
        # 모든 words에 있는 단어는 2글자로 이루어져 있는 상황이다.
        check = defaultdict(int)
        cnt = 0
        single = False
        word_map = defaultdict(int)
        ## 자기 자신이 palindrome이 되는 경우에는 무조건 제일 홀수개가 많은 애를 가운데에 배치를 하고 나머지는 짝수개인 경우에는 짝수개씩 배치하면 된다.
        self_odd, self_even = [], []
        for word in words:
            word_map[word] += 1
            if check[word] == 0:
                check[word] = 1
        for word in list(set(words)):
            if word[::-1] == word:
                check[word] = 0
                if word_map[word] % 2 == 0: ## 짝수개인 경우
                    self_even.append(word_map[word])
                else: ## 홀수개인 경우
                    self_odd.append(word_map[word])
        self_odd = sorted(self_odd, reverse = True)
        cnt += sum(self_even) * 2
        if self_odd:
            cnt += self_odd[0] * 2
            for n in self_odd[1:]:
                cnt += (n // 2) * 4
    
        
        for word in list(set(words)):
            if check[word] == 0:
                continue
            if word[::-1] == word: ## 자기 자신이 palindrome인 경우
                continue
            elif word[::-1] in words:
                cnt += 4 * (min(word_map[word], word_map[word[::-1]]))
                check[word] = check[word[::-1]] = 0
        return cnt


    def leastInterval(self, tasks, n):
        """
        - Given Characters array 'tasks', representing the tasks a CPU needs to do, where each letter represents a different task.
        - Tasks could be done in any order.
        - 주어진 수 n이 같은 종류의 task 사이에 있을 수 있는 최소한의 시간이다.
        - 정답 = busy slots + idle slots
        """
        task_map = defaultdict(int)
        answer = len(tasks)
        for task in tasks:
            task_map[task] += 1
        rep = max(list(task_map.values()))

        idle_time = (rep - 1) * n ## 최대로 필요한 idle이 필요한 개수를 의미한다

        times = sorted(list(task_map.values()), reverse = True) ## 각각의 task의 빈도수를 내림차순으로 정렬을 한다.
        for t in times[1:]:
            idle_time -= min((rep - 1), t) ## decrease the idle time by min(f_max - 1, f) 
            idle_time = max(idle_time, 0) ## idle_time must be greater than or same as 0
        return answer + idle_time
        
        




        

if __name__ == "__main__":
    sol = Solution()
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    print(sol.leastInterval(tasks, n))
