class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def backtracking(i, total):
            if total > amount or i == len(coins):
                return 0
            elif (i, total) in memo:
                return memo[(i, total)]
            elif total == amount:
                return 1

            
            include = exclude = 0
            #exclude
            exclude += backtracking(i + 1, total)

            #include
            include += backtracking(i, total + coins[i])
            memo[(i, total)] = include + exclude
            return memo[(i, total)]
        
        return backtracking(0, 0)
            