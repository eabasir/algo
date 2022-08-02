# Given an array of A, find the longest sub array all of whose entries are equal
import math


class Solution():

    def longest_sub_array(self, A: list[int]) -> list[int]:

        if(len(A) == 0):
            return []

        if(len(A) == 1):
            return A

        A1 = A[:math.ceil(len(A)/2)]
        A2 = A[math.ceil(len(A)/2):]

        longest_A1 = self.longest_sub_array(A1)
        longest_A2 = self.longest_sub_array(A2)

        if(longest_A1 == longest_A2):
            return longest_A1 + longest_A2
        else:
            return longest_A1 if len(longest_A1) >= len(longest_A2) else longest_A2


A = [1, 3, 2, 5, 5, 6, 1, -1, 4, 5, 0, -2]
res = Solution().longest_sub_array(A) == [5, 5, 5]
