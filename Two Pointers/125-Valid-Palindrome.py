class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not len(s):
            return False
        
        s = re.sub(r\[^a-zA-Z0-9]\, \\, s).lower()
        # from here we can rather than using this variables
        # make it much smaller by:
        # return (s==s[::-1])
        start = 0
        end = len(s) - 1
        while (start < end):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
