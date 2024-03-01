class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        maxLength = 0

        while s[j] == " ":
            j -= 1
        while j >= 0 and s[j] != " ":
            maxLength += 1
            j -= 1
        return maxLength