class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqele = {}

        for n in nums:
            if n in freqele:
                freqele[n] += 1
            else:
                freqele[n] = 1
        
        sorted_freqele = sorted(freqele, key = freqele.get, reverse = True)
        return sorted_freqele[:k]