class Solution:
    # @return an integer
    """
    Given a string, find the length of the longest substring without repeating characters.
    For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
    For "bbbbb" the longest substring is "b", with the length of 1.
    """
    def lengthOfLongestSubstring(self, s):
        # m = 1
        # for i in range(0, len(s)-1):
        #     j = i + 1
        #     c = s[j]
        #     while c not in s[i:j]:
        #         if j < len(s)-1:
        #             j += 1
        #         else:
        #             break
        #         c = s[j]
        #     if m < j-i:
        #         m = j-i
        # return m
        l = 0
        r = 1
        m = 1
        while l <= r < len(s):
            if s[r] not in s[l:r]:
                r += 1
                m = max(m, r-l)
            else:
                l += 1
        return m




if __name__ == '__main__':
    s = "abcabc"
    test = Solution()
    n = test.lengthOfLongestSubstring(s)
    print(n)