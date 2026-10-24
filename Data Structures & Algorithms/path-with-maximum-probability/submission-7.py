class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for (u, v), w in zip(edges, succProb):
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        probs = [0] * n
        probs[start_node] = 1
        heap = [(-1, start_node)]
        visted = set()
        while heap:
            curr_prob, u = heapq.heappop(heap)
            curr_prob *= -1

            if u in visted:
                continue
            if u == end_node:
                break
            visted.add(u)

            
            for v, w in graph[u]:
                new_prob = w * curr_prob
                if new_prob >= probs[v]:
                    probs[v] = new_prob
                    heapq.heappush(heap, (-new_prob, v))
        

        return probs[end_node]