class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        sorted_res = sorted(count.items(),key=lambda item:item[1],reverse=True)
        for i in range(k):
            u,w = sorted_res[i]
            res.append(u)

        return res
        