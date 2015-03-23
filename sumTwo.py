class Solution:
    def twoSum(num, target):
        t = {}
        for i, n in enumerate(num):
            t[n] = i
        print(t)
        for i, n in enumerate(num):
            a = target - n
            if a in t:
                b = t[a]
                if i < b:
                    return (i+1, b+1)
                elif b < i:
                    return (b+1, i+1)

if __name__ == '__main__':
    num = {1, 2, 5, 9}
    target = 7
    print(Solution.twoSum(num, target))