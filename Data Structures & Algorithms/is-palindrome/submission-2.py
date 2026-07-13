class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
        l = 0
        r = len(s)-1
        while l < r:
            while l<r and not alphaNum(s[l]):
                l+=1
            while l<r and not alphaNum(s[r]):
                r-=1
            if s[r].lower() != s[l].lower():
                return False
            r-=1
            l+=1

            
        return True
    
        
        