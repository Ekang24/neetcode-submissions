
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+' : lambda a,b: a+b,
            '-' : lambda a,b: a-b,
            '*' : lambda a,b: a*b,
            '/' : lambda a,b: int(a/b)}
        for char in tokens:
            if char in operators:
                b = stack.pop()
                a = stack.pop()
                result = operators[char](a,b)
                stack.append(result)
            else:
                stack.append(int(char))

                
        return stack[-1]
            

        
        