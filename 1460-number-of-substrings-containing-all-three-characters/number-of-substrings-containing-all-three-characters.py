class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if s == "abc":
            return 1
        n = len(s)
        hasher = {"a":0,"b":0,"c":0}
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in hasher:
                hasher[s[r]] += 1
            else:
                hasher[s[r]] = 1
            while hasher["a"]>0 and hasher["b"]>0 and hasher["c"]>0:
                ans += n-r
                # print(hasher)
                if hasher[s[l]]>1:
                    hasher[s[l]] -= 1
                else:
                    hasher[s[l]] = 0
                    
                l += 1
        return ans