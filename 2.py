# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listToLinkedList(self, l):
        l = [ListNode(i) for i in l]
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        return l[0]

    def linkedListToList(self, l):
        if l == None:
            return []
        node = l
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        l = ListNode(None)
        s = l
        carry = 0
        while True:
            if l1 == None:
                summation = carry + l2.val
                if summation > 9:
                    if l2.next:
                        l2.next.val += 1
                l.next = l2
                break
            elif l2 == None:
                l.next = l1
                break
            else:
                node = ListNode(None) # 临时node
                summation = l1.val + l2.val + carry # 算出和
                print(summation)
                if summation > 9: # 如果和有进位
                    carry = 1
                    node.val = summation - 10
                else:
                    carry = 0
                    node.val = summation
                l1 = l1.next # 到下一格
                l2 = l2.next # 到下一格
                l.next = node # 把临时node串起来
                l = l.next # 到下一格
            
        return s.next

l1 = [ListNode(i) for i in [1]]
for i in range(len(l1) - 1):
    l1[i].next = l1[i + 1]

l2 = [ListNode(i) for i in [9, 9]]
for i in range(len(l2) - 1):
    l2[i].next = l2[i + 1]

l = l1[0]
while l:
    print(l.val)
    l = l.next

solution = Solution()
print(solution.linkedListToList(l1[0]))
print(solution.linkedListToList(solution.listToLinkedList([1, 2, 3])))

l = Solution().addTwoNumbers(l1[0], l2[0])
while l:
    print(l.val)
    l = l.next