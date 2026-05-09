class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_length = len(nums)
        new_length = len(list(set(nums)))

        if original_length == new_length:
            return False
        
        return True