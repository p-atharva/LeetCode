import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])
        
        heapq.heapify(minHeap)
        finalResult = []

        while k > 0:
            d, x, y = heapq.heappop(minHeap)
            finalResult.append([x,y])
            k -= 1
        
        return finalResult


        