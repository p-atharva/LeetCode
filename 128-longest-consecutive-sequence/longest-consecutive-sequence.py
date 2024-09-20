class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)     #time = O(n)
        longest_sequence = 0

        for n in nums:
            if (n-1) not in nums_set:
                length_of_sequence = 1
                while (n+length_of_sequence) in nums_set:
                    length_of_sequence += 1
                longest_sequence = max(length_of_sequence, longest_sequence)
        
        return longest_sequence
        
        