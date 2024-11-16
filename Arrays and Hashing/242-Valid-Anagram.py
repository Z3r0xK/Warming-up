class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False
        
        stringS, stringT = {} , {}
        for i in range(len(s)):
            stringS[s[i]] = stringS.get(s[i], 0) + 1
            stringT[t[i]] = stringT.get(t[i], 0) + 1
        

        return stringS == stringT