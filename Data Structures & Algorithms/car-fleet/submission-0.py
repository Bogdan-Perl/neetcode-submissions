from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car as (position, time_to_target), sort by position descending
        cars = sorted(
            ((p, (target - p) / s) for p, s in zip(position, speed)),
            key=lambda x: -x[0]
        )

        stack = []  # will store times; it’s effectively nondecreasing from bottom to top
        for _, t in cars:
            # If this car takes longer than the fleet ahead, it forms a new fleet
            if not stack or t > stack[-1]:
                stack.append(t)
            # else: it merges into the fleet ahead (do nothing)

        return len(stack)
