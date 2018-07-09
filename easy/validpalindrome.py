import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()

        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    res = s.isPalindrome('A man, a plan, a canal: Panama')
    print(res)