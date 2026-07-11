class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for idx,num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                pop = stack.pop()
                res[pop[1]] = idx - pop[1]
            stack.append([num,idx])
        return res
                    

            


        