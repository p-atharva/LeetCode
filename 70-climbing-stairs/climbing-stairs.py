class Solution:
    def climbStairs(self, n: int) -> int:
        one_before, last = 1, 1      #no. of way to reach the n from n-1 and n itself. If starting backwards

        #Basically we are doing fibonacci series but from n to 0, which we have to compute n-1 time in total
        for i in range(n - 1):
            temp = one_before
            one_before =  one_before + last
            last = temp
        
        return one_before

        