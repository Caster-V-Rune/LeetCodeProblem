# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def encode(self, num):
        head = ListNode(num % 10)
        p = head
        num = (num - num % 10) / 10
        while num != 0:
            p.next = ListNode(num % 10)
            p = p.next
            num = (num - num % 10) / 10
        return head

    def decode(self, head):
        num = 0
        p = head
        i = 0
        while p is not None:
            num += p.val * math.pow(10, i)
            p = p.next
            i += 1
        return num

    def addTwoNumbers(self, l1, l2):
        n1 = self.decode(l1)
        n2 = self.decode(l2)
        ans = n1 + n2
        return self.encode(ans)


if __name__ == '__main__':
    test = Solution()
    a = test.encode(777)
    b = test.encode(123)
    print(test.decode(test.addTwoNumbers(a, b)))
