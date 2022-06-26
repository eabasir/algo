# return a possible combination of elements of an array that add up to a target
# time complexity: O(N*Mˆ3) => M = target , N = number of elements
# space complexity: O(Mˆ3)

class Solution:

    memo = {}

    def how_sum(self, target, numbers):

        if target == 0:
            return []

        if target < 0:
            return None

        res = []
        for idx, number in enumerate(numbers):
            remainder = target - number
            new_numbers = numbers[:idx] + numbers[idx+1:]

            self.memo[remainder] = self.how_sum(remainder, new_numbers)
            if(self.memo[remainder] is not None):
                if (len(self.memo[remainder]) == 0):
                    res.append([number])
                else:
                    for path in self.memo[remainder]:
                        res.append([*path, number])

        return res if len(res) != 0 else None


solution = Solution()
print(solution.how_sum(5, [2, 3, 1, 1]))
