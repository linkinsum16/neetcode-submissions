class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for item in strs:
            sortedI = ''.join(sorted(item))
            result[sortedI].append(item)
        return list(result.values())
