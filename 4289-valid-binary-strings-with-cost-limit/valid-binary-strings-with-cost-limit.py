class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        bins = list()
        # def cost(s):
        #     curr = 0
        #     # s = list(s)
        #     for i, ele in enumerate(s):
        #         if ele == "1":
        #             curr += i
        #         if curr >k:
        #             return k+1
        #     return curr

        def generateStrings(s, cost):

            if cost > k:
                return
            if len(s) == n:
                bins.append(s)
                return 
            generateStrings(s + "0", cost)
            if not s or s[-1] != "1":
                generateStrings(s + "1", cost+len(s))
        generateStrings("",0)
        # print(bins)
        return bins
