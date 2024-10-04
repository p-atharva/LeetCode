import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #preprocessing the array for Heapify (negating the values, to create minHeap)
        for s in range(len(stones)):
            stones[s] = -stones[s]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
            
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0

        
        