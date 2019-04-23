"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle
解决办法，草丛第一个元素开始每个元素都代表后面的一个集合
这题怪我没把题目看清，我还以为要用子集的坐标
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
