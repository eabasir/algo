class Solution():

    def how_many_advance(self, vals):
        i, furthest_advance_sofar, last_index = 0, 0, len(vals) - 1
        steps = 0
        while(i <= furthest_advance_sofar and furthest_advance_sofar < last_index):
            new_furthest_advance = max(vals[i] + i, furthest_advance_sofar)
            if(new_furthest_advance != furthest_advance_sofar):
                furthest_advance_sofar = new_furthest_advance
                steps += 1
            i += 1

        return steps if new_furthest_advance >= last_index else None


assert Solution().how_many_advance([3, 2, 1, 0, 1]) == None
assert Solution().how_many_advance([3, 1, 0, 1]) == 1
assert Solution().how_many_advance([3, 5, 0, 1]) == 1
assert Solution().how_many_advance([1, 1, 1, 1, 1, 0, 1]) == None
assert Solution().how_many_advance([1, 1, 1, 1, 1, 1, 1]) == 6
assert Solution().how_many_advance([3, 1, 1, 2, 1, 1, 1]) == 3
