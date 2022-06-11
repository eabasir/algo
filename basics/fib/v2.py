# fibonacci with DP

class Solution:

    def __init__(self):
        self.vals = {}

    def get_value(self, n):
        if n in self.vals:
            return self.vals[n]

        self.vals[n] = self.fib(n)
        return self.vals[n]
        

    def fib(self, n):
        if n <= 2:
            self.vals[n] = 1
            return 1
        return self.get_value(n - 1) + self.get_value(n - 2)



assert Solution().fib(7) == 13
assert Solution().fib(8) == 21
print(Solution().fib(100))