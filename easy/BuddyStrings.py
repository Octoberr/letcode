'''
Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
'''


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        # 完全相等且每个元素都相等
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))

            if len(pairs) > 2:
                return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

if __name__ == '__main__':
     A ="aaaaaaabc"
     B = "aaaaaaacb"
     s = Solution()
     res = s.buddyStrings(A, B)
     print(res)
