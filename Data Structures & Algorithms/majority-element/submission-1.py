class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        score = 0
        candidate = 0

        for num in nums:

            if score == 0:
                candidate = num
                score = 1
            
            if num == candidate:
                score += 1
            else:
                score -= 1

        return candidate

        