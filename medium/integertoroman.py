"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
create by swm 2018/05/31

"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        c={0:("","I","II","III","IV","V","VI","VII","VIII","IX"),
           1:("","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"),
           2:("","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"),
           3:("","M","MM","MMM")}
        roman=[]
        roman.append(c[3][num//1000%10])
        roman.append(c[2][num//100%10])
        roman.append(c[1][num//10%10])
        roman.append(c[0][num%10])
        s=''
        for i in roman:
            s=s+i
        return s


if __name__ == '__main__':
    s = Solution()
    re = s.intToRoman(454)
    print(re)
