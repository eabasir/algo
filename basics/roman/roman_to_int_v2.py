# more general solution when:
# smaller digits act as negative when they come before the larger ones

class Solution:

    vals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        total = 0
        idx = 0
        while idx < len(s):
            sign = 1
            if(idx < len(s) - 1):
                sign = 1 if self.vals[s[idx]] >= self.vals[s[idx + 1]] else -1
            else:
                sign = 1

            total = total + sign * self.vals[s[idx]]
            idx = idx + 1
        return total


assert Solution().romanToInt('III') == 3
assert Solution().romanToInt('LVIII') == 58
assert Solution().romanToInt('MCMXCIV') == 1994
