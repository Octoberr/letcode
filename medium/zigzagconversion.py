"""
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I
   这题只是简单的字符串处理。首先，我们可以对Z形字符串进行简单优化一下，将Z中的“折”合起来。比如：“ABCDEFGHIJKL”，4

A	 	 	G
B	 	F	H	 	L
C	E	 	I	K
D	 	 	J
优化后：

A	 	G
B	F	H	L
C	E	I	K
D	 	J
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        if size <= numRows or numRows == 1:
            return s
        ans = ''
        i = 0
        while i < numRows:
            j = i
            if i == 0 or i == numRows - 1:
                while j < size:
                    ans += s[j]
                    j += 2*numRows - 2
                    if 2 * numRows - 2 == 0:
                        break
            else:
                while j < size:
                    ans += s[j]
                    j += 2*(numRows - i) - 2
                    if j >= size:
                        break
                    ans += s[j]
                    j += 2*i
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    res = s.convert('PAYPALISHIRING', 4)
    print(res)
