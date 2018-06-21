"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
create by swm
2018/06/08
最终将3Sum拆解为2Sum+X，2Sum可以先排序，然后再用收尾慢慢收缩的方式寻找target，并且可以在寻找时剔除相同的left，right，时间复杂度因为O(N)。在3Sum中，则需要每个nums[]中的元素都作为X一次
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        first=[]
        i=0
        while(i<len(nums)-2):
            if(nums[i]!=nums[i-1] or i==0):
                target=0-nums[i]
                left=i+1
                right=len(nums)-1
                while(left!=right):
                    if(nums[left]+nums[right]==target):
                        first.append([nums[i],nums[left],nums[right]])
                        while(left<right):
                            left+=1
                            if(nums[left]!=nums[left-1]):
                                break
                        while(right>left):
                            right-=1
                            if(nums[right]!=nums[right+1]):
                                break
                    elif(nums[left]+nums[right]>target):
                        right-=1
                    elif(nums[left]+nums[right]<target):
                        left+=1
            i+=1
        return first