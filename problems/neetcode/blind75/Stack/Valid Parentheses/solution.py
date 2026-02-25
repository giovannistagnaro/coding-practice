class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c in bracket_map.values():
                stack.append(c)
            else:
                if len(stack) < 1 or stack.pop() != bracket_map[c]:
                    return False
                
        return True if len(stack) == 0 else False