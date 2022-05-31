# Time: O(log x)
# Space: O(1)

# forming L and R value and comparing them

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        L = x
        R = 0

        while L > R:
            R = R*10 + L % 10
            L = L // 10
        
        return L == R or L == R // 10

        
assert Solution().isPalindrome(1221) == True
assert Solution().isPalindrome(12321) == True
assert Solution().isPalindrome(31) == False
assert Solution().isPalindrome(-121) == False
assert Solution().isPalindrome(8) == True

