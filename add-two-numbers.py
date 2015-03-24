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
            num = num + p.val * math.pow(10, i)
            p = p.next
            i += 1
        return num

    def test(self, a, b):
        h1 = self.encode(a)
        h2 = self.encode(b)
        n1 = self.decode(h1)
        n2 = self.decode(h2)
        return n1, n2

    def addTwoNumbers(self, l1, l2):
        a = self.decode(l1)
        b = self.decode(l2)
        c = a + b
        return self.encode(c)

if __name__ == '__main__':
    test = Solution()
    a = test.encode(777)
    b = test.encode(123)
    print(test.decode(test.addTwoNumbers(a, b)))