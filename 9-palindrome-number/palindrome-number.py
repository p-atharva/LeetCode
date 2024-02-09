class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = list(map(str, str(x)))
        
        if temp[::1] == temp[::-1]:
            return True