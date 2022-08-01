# Given a sorted array A and a x positive integer that is repeated m times,
# change the Array in one pass with linear complexity so that the max occurrence of x in the array would be min(2,m)

class Solution():

    def max_2_occurrence(self, A: list[int], x: int):

        i, write_index, occurrence = 0, 0, 0
        while(i < len(A)):
            if(A[i] == x):
                occurrence += 1
                if(occurrence <= 2):
                    A[write_index] = A[i]
                    write_index += 1
            else:
                A[write_index] = A[i]
                write_index += 1

            i += 1

        while(write_index < len(A)):
            A[write_index] = None
            write_index += 1
        return A


A = [-3, -2, -1, 0, 1, 1, 1, 2, 3, 3, 3]
Solution().max_2_occurrence(A, 1)

assert A == [-3, -2, -1, 0, 1, 1, 2, 3, 3, 3, None]
