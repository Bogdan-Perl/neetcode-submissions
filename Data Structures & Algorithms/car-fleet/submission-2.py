class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(
            ((p, (target-p)/s) for p, s in zip(position, speed)),
            key = lambda x : -x[0]
        )
        stack = [] # increasing stack by time

        for _, t in cars:
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
