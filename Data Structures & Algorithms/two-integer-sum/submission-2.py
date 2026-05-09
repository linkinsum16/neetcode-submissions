class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find_dict = {}

        for i , num in enumerate(nums):
            compliment = target - num

            if compliment in find_dict:
                return [find_dict[compliment],i]
            find_dict[num] = i