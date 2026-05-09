class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        # Step 1: Build frequency map
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1

        result = []

        # Step 2: Find top k elements manually
        for _ in range(k):
            max_key = None
            max_count = -1

            # Find element with maximum count
            for key in freq_map:
                if freq_map[key] > max_count:
                    max_count = freq_map[key]
                    max_key = key

            result.append(max_key)

            # Remove or invalidate this key so it doesn't get picked again
            freq_map[max_key] = -1

        return result
