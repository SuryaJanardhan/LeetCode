class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        cnt = 0
        for i in range(len(nums)):
            if cnt != nums[i]:
                ans = ans & nums[i]

            cnt += 1

        return 0 if ans == -1 else ans