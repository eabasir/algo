# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        if n < 0:
            return 0
        
        return self.climbStairs(n -2) + self.climbStairs(n - 1)




# assert Solution().climbStairs(3) == 3
print ( Solution().climbStairs(3)) 