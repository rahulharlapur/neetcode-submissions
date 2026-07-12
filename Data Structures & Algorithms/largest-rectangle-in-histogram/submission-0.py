class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                pop = stack.pop()
                area = pop[1] * (i-pop[0])
                max_area = max(max_area,area)
                start = pop[0]
            stack.append([start,heights[i]])
        
        for i,h in stack:
            max_area = max(max_area,h*(len(heights)-i))
        return max_area

            