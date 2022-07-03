from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        lcp = strs[0]
        for i in range(1, len(strs)):
            tmp = ""
            for j in range(len(lcp)):

                if(j == len(strs[i])):
                    break

                if (lcp[j] != strs[i][j]):
                    break

                tmp = tmp + lcp[j]

            lcp = tmp

        return lcp

    def getLen(self, arr):
        print(len(arr))
        return len(arr)


assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert Solution().longestCommonPrefix(["ab", "a"]) == "a"
assert Solution().longestCommonPrefix(["ab", ""]) == ""
