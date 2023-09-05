class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,m = 0,0

        while l < len(s) and m <len(t):
            if s[l] == t[m]:
                l += 1
                m += 1
            else:
                m += 1

        if l == len(s):
            return True
        else:
            return False