"""Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        return len(s.strip().split(' ')[-1])
if __name__ == '__main__':
    s = Solution()
    b = s.lengthOfLastWord('a')
    print(b)
