## Linked List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):
        # return True if palindrome or false otherwise
        nums = []
        while (head is not None):
            nums.append(head.val)
            head = head.next
        for i in range(len(nums)):
            left, right = i, len(nums) - i - 1
            if nums[left] != nums[right]:
                return False
        return 
        
    def removeNthFromEnd(self, head, n):
        length = 1
        temp_head = head
        nums = []
        while (temp_head.next is not None):
            nums.append(temp_head.val)
            temp_head = temp_head.next
            length += 1
        nums.append(temp_head.val)
        ## 이제 temp_head가 마지막이다.
        end = ListNode(val = -1)

        for i in range(length):
            if i == n:
                continue
            else:
                prev_ = ListNode(val = nums[length - i - 1])
                if end.val == -1:
                    end = prev_
                else:
                    prev_.next = end
                    end = prev_
        if end.val == 0:
            return None
        else:
            return end




            
            
        
        
        
        

        

