# can sum with DP

class Solution:

    memo = {}

    def canSum(self, target, numbers):

        if target == 0:
            return True
        if target < 0:
            return False

        for idx, number in enumerate(numbers):
            remainder = target - number
            new_numbers = numbers[:idx] + numbers[idx+1:]

            self.memo[remainder] = self.canSum(remainder, new_numbers)
            if (self.memo[remainder]):
                return True

        return False


assert Solution().canSum(4, [2]) == False
assert Solution().canSum(4, [1, 1, 1]) == False
assert Solution().canSum(4, [2, 2]) == True
assert Solution().canSum(4, [4]) == True
assert Solution().canSum(5, [2, 2, 3, 5, 6]) == True
assert Solution().canSum(5, [3, 1, 1]) == True
