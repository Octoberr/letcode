"""

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i*i:n:i] = [0] * int((n-i*i-1)/i + 1)
        return sum(s)


if __name__ == '__main__':
    s = Solution()
    res = s.countPrimes(10)
    print(res)