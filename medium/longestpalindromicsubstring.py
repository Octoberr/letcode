"""
找到最长的回文字符串
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
遍历字符串，假设把当前遍历到的元素当做回文中间数。当最长回文长度是偶数的，
那么中间数应该和下个数相等，然后其余的数都对称相等；当最长回文长度是奇数的，
那么其余的数应都对称相等。
"""


class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        # write your code here
        res = ''
        if s is None or len(s) == 0:
            return res
        for i in range(len(s)):
            j = i - 1
            k = i + 1
            tmp = s[i]
            while k < len(s) and s[k] == s[i]:
                tmp = tmp + s[k]
                k += 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                tmp = s[j] + tmp + s[k]
                j -= 1
                k += 1
            if len(tmp) > len(res):
                res = tmp
        return res


if __name__ == '__main__':
    s = Solution()
    a = 'cbbd'
    print(s.longestPalindrome(a))