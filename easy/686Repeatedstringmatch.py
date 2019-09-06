"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""


from collections import Counter
import math

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if not set(B).issubset(set(A)):
                return -1

        base = math.ceil(len(B) / len(A))
        for i in range(2):
            if B in A*(base + i):
                return base + i
        return -1


if __name__ == '__main__':
    A = 'abcd'
    B = 'cdabcdab'
    s = Solution()
    print(s.repeatedStringMatch(A,B))
