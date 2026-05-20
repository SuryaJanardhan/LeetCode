class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()
        ans = []
        for i in range(len(A)):
            a.add(A[i])

            b.add(B[i])
            temp = a & b
            ans.append(len(temp))
        return ans

        