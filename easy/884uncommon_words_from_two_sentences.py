"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]

使用集合解决
^对称差集
A, B = A.split(), B.split()
return (set(A) ^ set(B)) - set(a for a in A if A.count(a) > 1) - set(b for b in B if B.count(b) > 1)
"""


class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        a = {}
        allstr = A + ' ' + B
        aslist = allstr.split(' ')
        for el in aslist:
            if a.__contains__(el):
                a[el] += 1
                continue
            a[el] = 1

        reslist = [k for k, v in a.items() if v == 1]
        return reslist
if __name__ == '__main__':
    s = Solution()
    A = "apple apple"
    B = "banana"
    res = s.uncommonFromSentences(A, B)
    print(res)
