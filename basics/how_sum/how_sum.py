# return a possible combination of elements of an array that add up to a target
# time complexity: O(Nˆ2*Mˆ2) => M = target , N = number of elements // TODO: Nˆ2 as we slice the array in for loop so there is an extra N?
# space complexity: O(Nˆ2*Mˆ2) // TODO: in each call a new array is created (by slice) so the original array is not passed downside by reference. that means in worst case,
# arrays of sizes: 1,2,3,...,N are save on memory which is Nˆ2

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
print(solution.how_sum(5, [1]))
