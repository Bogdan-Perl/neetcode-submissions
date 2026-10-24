class TimeMap:

    def __init__(self):
        self.items = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.items:
            self.items[key] = []
        self.items[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        vals = self.items.get(key, [])
        if not vals or vals[0][0] > timestamp:    
            return ""
        L, R = 0, len(vals) - 1
        res = ""
        while L <= R:
            M = (L + R) // 2
            
            t, v = vals[M]
            if t <= timestamp:
                res = v
                L = M + 1
            else:
                R = M - 1
        return res
            

        
