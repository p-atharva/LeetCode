import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #time complexity = O(N logk)
        #space complexity = O(k)

        minHeap = []
        
        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            else:
                heapq.heappushpop(minHeap, n)
        
        return minHeap[0]