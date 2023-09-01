class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1
        while lp < rp:
            while lp < rp and not self.checkalphaNum(s[lp]):
                lp += 1
            while rp > lp and not self.checkalphaNum(s[rp]):
                rp -= 1
            if s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1
        return True

    def checkalphaNum(self, ch):
        return (ord("A") <= ord(ch) <= ord("Z") or
                ord("a") <= ord(ch) <= ord("z") or
                ord("0") <= ord(ch) <= ord("9"))