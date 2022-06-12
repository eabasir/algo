# can sum without DP

class Solution:
    def canSum(self, target, numbers, ignored_index=0):

        if target == 0:
            return True
        if target < 0:
            return False

        for idx, number in enumerate(numbers):
            if idx == ignored_index and target != number:
                continue

            remainder = target - number
            if (self.canSum(remainder, numbers, idx)):
                return True

        return False


assert Solution().canSum(4, [2]) == False
assert Solution().canSum(4, [2, 2]) == True
assert Solution().canSum(4, [4]) == True
assert Solution().canSum(5, [2, 2, 3, 5, 6]) == True
