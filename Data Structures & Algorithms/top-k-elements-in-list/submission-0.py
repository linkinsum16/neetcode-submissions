class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(list)
        res = []
        for num in nums:
            if num in result:
                result[num]+=1
            else:
                result[num] = 1
        result = sorted(result.items(), reverse=True, key=lambda x: x[1])
        for key,value in result:
            res.append(key)
        return res[:k]