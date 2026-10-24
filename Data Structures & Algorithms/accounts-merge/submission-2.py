class DSU:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [0] * N

    def find(self, n):
        while n != self.par[n]:
            n = self.par[self.par[n]]
        return self.par[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = DSU(len(accounts))

        emToAct = {}

        for idx, a in enumerate(accounts):
            for e in a[1:]:
                if e in emToAct:
                    uf.union(idx, emToAct[e])
                else:
                    emToAct[e] = idx

        emailGroup = defaultdict(list)
        for e, i in emToAct.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res




















        