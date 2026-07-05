class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        heap = []

        for key,val in count.items():
            heapq.heappush(heap,(val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        