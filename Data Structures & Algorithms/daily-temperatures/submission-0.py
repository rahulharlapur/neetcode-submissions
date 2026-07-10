class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            count = 0 
            j= i+1
            while j<len(temperatures):
                if temperatures[j] > temperatures[i]:
                    count+=1
                    res[i] = count
                    break
                else:
                    count+=1
                    j+=1
        return res


        