import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countOfEach = Counter(tasks)
        #creating a max heap
        maxHeap = [-cnt for cnt in countOfEach.values()]

        heapq.heapify(maxHeap)

        time = 0
        q = deque()         #storing the remaining occurances and the future time we can visit it.

        while maxHeap or q:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

        