import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #time complexity = O(N logk)
        #space complexity = O(k)
        #using min heap to solve this question. This can also be solved using max heap

        minHeap = []
        
        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            else:
                heapq.heappushpop(minHeap, n)
        
        return minHeap[0]