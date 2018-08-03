"""

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = {
            "maxnum": count
        }
        for i in nums:

            if i != 0:
                count += 1
            else:
                if res['maxnum'] < count:
                    res['maxnum'] = count
                count = 0
        if res['maxnum'] < count:
            res['maxnum'] = count
        return res['maxnum']


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,0,1,1,1]
    res = s.findMaxConsecutiveOnes(nums)
    print(res)
