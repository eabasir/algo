# Time: O(log x)
# Space: O(log x)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = self.get_digits(x)
        for i in range(len(digits) // 2):
            if digits[i] != digits[len(digits) - i - 1]:
                return False

        return True

    def get_digits(self, x: int) -> list[int]:
        digits = []
        while (x != 0):
            digits.append(x % 10)
            x = x // 10

        return digits


assert Solution().isPalindrome(1221) == True
assert Solution().isPalindrome(31) == False
assert Solution().isPalindrome(-121) == False
assert Solution().isPalindrome(8) == True

