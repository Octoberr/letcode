"""
判断一个数是否是回文数
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        flag = True
        for i in range(len(a) // 2):
            if a[i] != a[-i - 1]:
                flag = False
                break
        return flag

if __name__ == '__main__':
    s = Solution()
    b = s.isPalindrome(1000021)
    print(b)