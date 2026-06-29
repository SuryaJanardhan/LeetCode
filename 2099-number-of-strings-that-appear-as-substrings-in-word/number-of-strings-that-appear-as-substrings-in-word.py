class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for w in patterns:
            if(w in word):
                c+=1
                
        return c        