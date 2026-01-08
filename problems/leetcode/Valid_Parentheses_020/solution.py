from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        paren_map = {')': '(', '}': '{', ']': '['}
        open_parens = set(paren_map.values())

        for paren in s: 
            if paren in open_parens:
                stack.append(paren)
            else:
                if stack and stack[-1] == paren_map[paren]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False