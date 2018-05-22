"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
byswm 2018/05/15
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

    def anthersun(self, nums, tar):
        lookup = dict((v, i) for i, v in enumerate(nums))
        res = next(((i, lookup.get(tar-v)) for i, v in enumerate(nums) if lookup.get(tar-v, i) != i), None)
        return res


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    t = Solution().anthersun(a, 6)
    print(t)
