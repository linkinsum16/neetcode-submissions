class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        counter = set()
        for item in nums:
            if item in counter:
                return True
            counter.add(item)
        return False
