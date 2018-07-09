"""

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
"""


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""
        else:
            res = self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))
            return res

        # return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))


if __name__ == '__main__':
    n = 701
    s = Solution()
    res = s.convertToTitle(n)
    print(res)