## LINKED LIST ##
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergesort(self, list1, list2):
        dummy = ListNode()
        ptr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        while list1:
            ptr.next = list1
            list1 = list1.next
            ptr = ptr.next
        while list2:
            ptr.next = list2
            list2 = list2.next
            ptr = ptr.next
        return dummy.next


    def sortList(self, head): 
        ## 예시에도 나와있듯이 비어있거나 1개의 node로만 구성된 경우에는 return head
        if not head or not head.next:
            return head
        ## linked list에서의 가운데 수를 찾아준다
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        right = mid.next ## right
        left = head
        mid.next = None
        sorted1 = self.sortList(left) ## sorted left list
        sorted2 = self.sortList(right) ## sorted right list

        return self.mergesort(sorted1, sorted2)
        

    def oddEvenList(self, head):
        """
        - 홀수번째 node와 짝수번째 node를 각각 서로 연결해 준다.
        """
        start = head
        odd, even = [], []
        cnt = 1
        while start is not None:
            if cnt % 2 == 0:
                odd.append(start.val)
            else:
                even.append(start.val)
            start = start.next
            cnt += 1
        final_list = even + odd
        answer = ListNode(val = 10 ** 7)
        for i in range(len(final_list)-1, -1, -1):
            if answer.val == 10**7:
                answer.val = final_list[i]
            else:
                new = ListNode(val = final_list[i])
                new.next = answer
                answer = new
        if answer.val == 10**7:
            return None
        return answer


            
            

