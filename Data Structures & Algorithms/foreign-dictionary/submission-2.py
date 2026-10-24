class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree = defaultdict(int)
        depgraph = defaultdict(list)
        for w in words:
            for ch in w:
                indegree.setdefault(ch, 0)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1] 
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in depgraph[c1]:
                        depgraph[c1].append(c2)
                        indegree[c2] += 1
                    break
            
        q = deque([ch for ch, deg in indegree.items() if deg == 0])
        order = []

        while q:
            ch = q.popleft()
            order.append(ch)

            for nei in depgraph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        res = "".join(order)
        return res if len(res) == len(indegree) else ""



