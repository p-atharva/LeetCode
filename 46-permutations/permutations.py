class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        f_ans , curr_ans = [], [] 

        def backtrack():
            if len(curr_ans) == n:
                f_ans.append(curr_ans[:])
                return

            for nu in nums:
                if nu not in curr_ans:
                    curr_ans.append(nu)
                    backtrack()
                    curr_ans.pop()
            
        backtrack()
        return f_ans

        