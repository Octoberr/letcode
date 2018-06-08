"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        if not height or len(height) == 1:
            return 0
        res = (r - l) * (height[l] if height[l] < height[r] else height[r])

        while l < r:
            if height[l] < height[r]:
                res = res if res > height[l] * (r - l) else height[l] * (r - l)
                l += 1
            else:
                res = res if res > height[r] * (r - l) else height[r] * (r - l)
                r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([2,4,1,5,3]))