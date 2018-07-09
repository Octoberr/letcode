"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
知识点注意：x^y是异或运算，不同为1，相同为0，bin()的结果是01字符串，求结果01字符串中的'1'字符的个数，就是hamming distance。
"""


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    s = Solution()
    res = s.hammingDistance(1, 4)
    print(res)