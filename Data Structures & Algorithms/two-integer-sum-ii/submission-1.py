class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers)-1
        while l<r:
            sum_of_no =numbers[r]+numbers[l]
            if sum_of_no == target:
                return [l+1,r+1]
            if sum_of_no<target:
                l+=1
            else:
                r-=1
