class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_seen = set()

        for num in nums:
            if num in is_seen:
                return True

            is_seen.add(num)
        return False