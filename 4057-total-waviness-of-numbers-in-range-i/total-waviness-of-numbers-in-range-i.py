class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        def waviness(n):
            n = list(str(n))
            waves = 0
            if len(n) < 3:
                return 0
            for i in range(len(n)-2):
                prev = int(n[i])
                after = int(n[i+2])
                curr = int(n[i+1])

                if prev < curr and curr > after:
                    waves += 1
                elif prev > curr and curr < after:
                    waves += 1
            return waves

        for i in range(num1, num2+1):

            ans += waviness(i)
        return ans