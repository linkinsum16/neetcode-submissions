class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}

        for x in s:
            if x in s_hashmap:
                s_hashmap[x] += 1
            else:
                s_hashmap[x] = 1
        for y in t:
            if y in t_hashmap:
                t_hashmap[y] += 1
            else:
                t_hashmap[y] = 1
        bigger_dict = s_hashmap if len(s_hashmap) > len(t_hashmap) else t_hashmap
        for key in bigger_dict.keys():
            if s_hashmap.get(key) != t_hashmap.get(key):
                return False
        return True
