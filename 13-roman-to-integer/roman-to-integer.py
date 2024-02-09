class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {"I": 1,"V": 5,"X":10,"L":50,"C": 100,"D": 500, "M": 1000}
        value = 0
        # i = 0
        # for i in range(len(s)):
        #     if i < len(s) -1 and translation[s[i]] < translation[s[i+1]]:
        #         value -= translation[s[i]]
        #     else:
        #         value += translation[s[i]]
        
        # return value 
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            value += translation[char]
        return value

        