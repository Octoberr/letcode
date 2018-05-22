"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
create by swm 2018/05/16
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        substring_map = {}
        start = 0
        for i in range(len(s)):
            position = substring_map.get(s[i])
            if position is not None and position >= start:
                length = i - start
                start = position + 1
                longest = max(length, longest)
            substring_map[s[i]] = i
        longest = max(len(s) - start, longest)
        return longest


if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLongestSubstring('abcabcbb'))


