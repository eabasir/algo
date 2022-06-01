# considering only the certain exceptions

class Solution:

    vals = {
        'M' : 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    exceptions = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        total = 0
        length = len(s)
        idx = 0
        while idx < length:
            
            if (idx < length -1):
                exception = self.exceptions.get(s[idx] + s[idx + 1], None)
                if ( exception != None):
                    total = total + exception
                    idx = idx + 2
                    continue 
            total = total + self.vals[s[idx]]
            idx = idx + 1
        return total

assert Solution().romanToInt('III') == 3
assert Solution().romanToInt('LVIII') == 58
assert Solution().romanToInt('MCMXCIV') == 1994