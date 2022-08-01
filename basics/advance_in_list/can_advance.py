class Solution():

    def can_advance(self, vals):
        i, furthest_advance_sofar, last_index = 0, 0, len(vals) - 1

        while(i <= furthest_advance_sofar and furthest_advance_sofar < last_index):
            furthest_advance_sofar = max(vals[i] + i, furthest_advance_sofar)
            i += 1

        return furthest_advance_sofar >= last_index


assert Solution().can_advance([3, 2, 1, 0, 1]) == False
assert Solution().can_advance([3, 1, 0, 1]) == True
assert Solution().can_advance([3, 5, 0, 1]) == True
assert Solution().can_advance([1, 1, 1, 1, 1, 0, 1]) == False
assert Solution().can_advance([1, 1, 1, 1, 1, 1, 1]) == True
