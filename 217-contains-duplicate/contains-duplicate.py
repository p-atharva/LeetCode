class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        convert_set = set()

        for n in nums:
            if n in convert_set:
                return True
            convert_set.add(n)
        return False
        