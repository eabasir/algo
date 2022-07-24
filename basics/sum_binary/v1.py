# sum two binary strings

class Solution:
    def sum(self, s1: str, s2: str) -> int:

        res = ''
        i1, i2 = len(s1) - 1, len(s2) - 1

        carry = 0

        while (i1 >= 0 and i2 >= 0):

            c1 = int(s1[i1]) if i1 >= 0 else 0
            c2 = int(s2[i2]) if i2 >= 0 else 0

            _sum = c1 + c2 + carry

            if(_sum >= 2):
                carry = 1
                res += str(_sum % 2)
            else:
                carry = 0
                res += str(_sum)

            i1 -= 1
            i2 -= 1

        if (carry > 0):
            res += '1'

        return res[::-1]


assert Solution().sum('00000', '00001') == '00001'
assert Solution().sum('111', '111') == '1110'
