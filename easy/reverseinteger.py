"""
给定一个 32 位有符号整数，将整数中的数字进行反转。
输入: 123
输出: 321
输入: -123
输出: -321
输入: 120
输出: 21
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x > 0:
            xdict = dict((i, v) for i, v in enumerate(str(x)))
            xdict['ope'] = '+'
            xdict['len'] = len(str(x))
        else:
            xdict = dict((i, v) for i, v in enumerate(str(x)[1:]))
            xdict['ope'] = '-'
            xdict['len'] = len(str(x))-1
        y = ''
        for i in reversed(range(xdict['len'])):
            if len(y) == 0 and xdict[i] == '0':
                continue
            y += xdict[i]
        if int(y) > 2**31:
            return 0
        if xdict['ope'] == '-':
            return -int(y)
        else:
            return int(y)


if __name__ == '__main__':
    s = Solution()
    b = s.reverse(1230)
    print(b)