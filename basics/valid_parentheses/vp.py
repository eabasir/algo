class Solution:

    pairs = {'{': '}', '(': ')', '[': ']'}

    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack: list = []

        for c in s:
            if(c in self.pairs):
                stack.append(self.pairs[c])
            # closing
            else:
                matched_closing = stack.pop() if len(stack) > 0 else ''
                if(matched_closing != c):
                    return False

        return len(stack) == 0


assert Solution().isValid('((') == False
assert Solution().isValid('())(()') == False
assert Solution().isValid('){') == False
assert Solution().isValid('[[()]]') == True
assert Solution().isValid('[(([]{}))]') == True
assert Solution().isValid('[(([]{})}]') == False
