"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true

正面排序
然后反面排序
牛P

"""


class Solution:
    def isMonotonic(self, A) -> bool:
        if sorted(A) == A:
            return True

        A.reverse()

        if sorted(A) == A:
            return True

        return False


if __name__ == '__main__':
    s = Solution()
    inputa = [6, 5, 4, 4]
    res = s.isMonotonic(inputa)
    print(res)
