class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #val -> index

        for  i,n in enumerate(nums):
            diff = target - n
            # print(diff)
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i