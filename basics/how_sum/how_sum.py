# return a possible combination of elements of an array that add up to a target

class Solution:

    memo = {}

    def how_sum(self, target, numbers):

        if target == 0:
            return []

        if target < 0:
            return None

        for idx, number in enumerate(numbers):
            remainder = target - number
            new_numbers = numbers[:idx] + numbers[idx+1:]

            self.memo[remainder] = self.how_sum(remainder, new_numbers)
            if(self.memo[remainder] is not None):

                return [*self.memo[remainder], number]

        return None


solution = Solution()
print(solution.how_sum(5, [1, 1, 2, 3]))
