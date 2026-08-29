class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
                "I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000
            }  
        ans = map[s[0]]
        for i in range(1, len(s)):
            curr = s[i]
            print("before",curr, ans)
            if 1:
                if curr == "V" and s[i-1] == "I":
                    ans += map[curr]
                    ans -= 2
                elif curr == "X" and s[i-1] == "I":
                    ans += map[curr]
                    ans -= 2
                elif curr == "L" and s[i-1] == "X":
                    ans += map[curr]
                    ans -= 20
                elif curr == "C" and s[i-1] == "X":
                    ans += map[curr]
                    ans -= 20
                elif curr == "M" and s[i-1] == "C":
                    ans += map[curr]
                    ans -= 200
                elif curr == "D" and s[i-1] == "C":
                    ans += map[curr]
                    ans -= 200
                else:
                    ans += map[curr]
            print("after",curr, ans)
           

        return ans