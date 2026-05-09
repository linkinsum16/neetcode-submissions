class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        counter = 2
        length = len(nums)
        while counter > 0:
            for i in range(0, length):
                ans.append(nums[i])
            counter -= 1

        return ans