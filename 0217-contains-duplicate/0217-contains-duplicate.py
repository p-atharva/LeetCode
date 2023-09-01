class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for ints in nums:
            if ints in hset:
                return True
            else: 
                hset.add(ints)
        return False