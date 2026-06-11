class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # parent - child dict 
        tree = {}
        parents = set()
        children = set()

        for i in edges:
            P = i[0]
            C = i[1]
            if P in tree:
                tree[P].append(C)
            else:
                tree[P] = [C]
            
            parents.add(P)
            children.add(C)

        root = parents - children

        def dfs(node):
            if node not in tree:
                return 0
            
            maxx = 0
            for i in tree[node]:
                maxx = max(maxx, 1+ dfs(i))
            return maxx
        maxx = dfs(list(root)[0])

        ans = 2**(maxx-1)
        return ans % (10**9+7)