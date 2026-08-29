class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
                "I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000
            }  
        ans = map[s[0]]
        for i in range(1, len(s)):
            curr = s[i]
            if map[curr] > map[s[i-1]]:
                ans += map[curr] - map[s[i-1]]*2
            else:
                ans += map[curr]
        return ans