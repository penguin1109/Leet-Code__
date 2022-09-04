## TREE ##
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalancedV2(self, root):
        self.answer = True
        def dfs(node):
            left, right = 0, 0
            if root.left:
                left += dfs(root.left)
            if root.right:
                right += dfs(root.right)
            if abs(left - right) > 1:
                self.answer = False
            return max(right, left) + 1
        dfs(root)
        return self.answer
                
            


    def dfs(self, node):
        if node is None:
            return 0
        else:
            return max(self.dfs(node.left), self.dfs(node.right)) + 1


    def isBalanced(self, root):
        """
        이 문제는 상당히 간단하게 풀릴 수 있는데, tree에 대해서 순회를 하고 매번 node마다 balance가 있는지 확인해야 한다.
        - dfs(node)를 계산하면 주어진 root node의 하위 트리의 높이를 return값으로 준다.
        - 만약에 balance tree라면 left sub-tree와 right sub-tree의 height의 차이가 무조건 1보다 적거나 같아야 한다.
        """
        if root is None:
            return True
        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)

        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(left_height - right_height) <= 1

    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
    
    def invertTree_rec(self, root):
        ## recursive solution: 재귀적으로 호출을 반복적으로 수행해서 이진 트리를 좌우 반전 시켜 준다.
        if root:
            root.left, root.right = self.invertTree_rec(root.right), self.invertTree_rec(root.left)
            return root

    def invertTree_exp(self, root):
        def lr_swap(node1, node2):
            temp = node1.left
            node1.left = node2.right
            node2.right = temp
            return node1, 
        def rl_swap(node1, node2):
            temp = node1.right
            node1.right = node2.left
            node2.left = temp
            return node1, node2
        """ Invert Binary Tree
        Given the root of a binary tree, invert the tree, and return its root
        """
        height = 0
        l, r = root.left, root.right
        while (l and r):
            nums = 2 ** height
            trial = nums // 2
            for t in range(trial):
                if t == 0:
                    continue
