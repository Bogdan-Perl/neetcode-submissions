class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                i = stack.pop()
                res[i] = idx - i
            stack.append(idx)
        return res
        