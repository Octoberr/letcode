"""
矩阵的转置
Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
"""


class Solution():
    def transpose(self, A):
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    s.transpose(a)