"""
链表求和
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# 列表写法
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        flag = 0
        res = []
        while l1 and l2:
            a = l1.pop()
            b = l2.pop()
            val = a + b + flag
            flag = val//10
            resa = val % 10
            res.append(resa)
        if l1:
            while l1:
                res.append(l1.pop())
        if l2:
            while l2:
                res.append(l2.pop())
        return res

# 链表写法
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        flag = 0
        dummy = ListNode(0); p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) // 10
            l1 = l1.next; l2 = l2.next; p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+flag) % 10)
                flag = (l2.val+flag) // 10
                l2 = l2.next; p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+flag) % 10)
                flag = (l1.val+flag) // 10
                l1 = l1.next; p = p.next
        if flag == 1: p.next = ListNode(1)
        return dummy.next

if __name__ == '__main__':
    a = [4, 2, 4, 3]
    b = [5, 6, 4]
    c = Solution().addTwoNumbers(a, b)
    print(c)