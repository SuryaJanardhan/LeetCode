class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        p1 = 0
        p2 = 0
        L , R = 0, len(nums)-1

        def recur(p1, p2, L, R, T):

            if L > R:
                return p1>=p2

            if T == 1:   
                return recur(p1 + nums[L], p2, L+1, R, 0) or recur(p1 + nums[R], p2, L, R-1, 0)
            else:           
                return recur(p1, p2 + nums[L], L+1, R, 1) and recur(p1, p2 + nums[R], L, R-1, 1)

        return recur(p1,p2,L, R ,1)