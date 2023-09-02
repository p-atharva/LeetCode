class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            lptr = 1
            
            for rptr in range(1, len(nums)):
                if nums[rptr] != nums[rptr -1]:
                    nums[lptr] = nums[rptr]
                    lptr +=1
            return lptr
        