class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for x in strs:
            sorted_str = "".join(sorted(x))

            if sorted_str not in result:
                result[sorted_str] = []
            
            
            result[sorted_str].append(x)

        
        return list(result.values())
