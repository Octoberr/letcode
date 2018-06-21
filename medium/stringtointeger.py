"""
实现 atoi，将字符串转为整数。

在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。
输入: "42"
输出: 42
"""

class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX = 2147483647; INT_MIN = -2147483648
        sum = 0
        sign = 1
        i = 0
        if str == '':
            return 0
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and str[i] == '-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            if INT_MAX/10 >= sum:
                sum *= 10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            if INT_MAX - digit >= sum:
                sum += digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1
        return sign*sum


if __name__ == '__main__':
    s = Solution()
    b = s.atoi('454545sad')
    print(b)
