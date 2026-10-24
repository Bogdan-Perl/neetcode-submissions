class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]
        cache = {}
        #state = (day, i )
        def memo(day, i):
            

            while i < len(days) and day > days[i]:
                i += 1
            if day > maxDay or i == len(days):
                return 0
            if day < days[i]:
                day = days[i]
            if (day, i) in cache:
                return cache[(day, i)]

            d = memo(day + 1, i + 1) + costs[0]
            w = memo(day + 7, i + 1) + costs[1]
            m = memo(day + 30, i + 1) + costs[2]
            
            cache[(day, i)] = (min(d, w, m))
            return cache[(day, i)]
        
        return memo(1, 0)


