class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        finalans = []
        for i in range(2):
            for n in nums:
                finalans.append(n)
        
        return finalans
        