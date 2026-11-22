class Solution:
    def checkString(self, s: str) -> bool:
        
        flag = 0
        for i in s:
            if flag and i == 'a':
                return False
            if i == 'b':
                flag = 1
        return True