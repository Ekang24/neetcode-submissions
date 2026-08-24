class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = ['+', 'C', 'D']
        for op in operations:
            if op not in ops:
                stack.append(int(op))
            elif op == '+':
                ans = stack[-1] + stack[-2]
                stack.append(ans)
            elif op == 'C':
                stack.pop()
            else:
                ans = stack[-1] * 2
                stack.append(ans)
        summ = 0
        while stack:
            
            summ += int(stack.pop())
        return summ