class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)
        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append([t, i ])
        return res
                


        

