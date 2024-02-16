class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputarr = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            outputarr[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            outputarr[i] *= postfix
            postfix *= nums[i]

        return outputarr
        