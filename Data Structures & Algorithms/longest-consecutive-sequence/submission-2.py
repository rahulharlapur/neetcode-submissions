class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count_map = {}
        len_res = 0
        for num in nums:
            count_map[num] = 1
        
        for key in list(count_map.keys()):
            if (key - 1) not in count_map:
                current_num = key
                current_streak = 1

                while (current_num + 1) in count_map:
                    current_num += 1
                    current_streak += 1

                len_res = max(len_res, current_streak)
        
        return len_res