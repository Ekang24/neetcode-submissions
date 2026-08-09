class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i,char in enumerate(s):
            if char in ('(', '{', '['):
                stack.append(char)
            if char in (')', '}', ']'):
                if not stack:
                    return False
                prev = stack.pop()
                if prev == '(' and char == ')':
                    continue
                elif prev == '{' and char == '}':
                    continue
                elif prev == '[' and char == ']':
                    continue
                return False
        return not stack
            
            
                

        