class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            res = nums.pop()
            nums.insert(0, res)


if __name__ == '__main__':
    nums = [1,2,34,2]
    k = 2
    s = Solution()
    s.rotate(nums, k)
    print(nums)