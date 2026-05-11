class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_hashmap = {}
        t_hashmap = {}

        for x in s:
            s_hashmap[x] = s_hashmap.get(x,0) + 1

        for y in t:
            t_hashmap[y] = t_hashmap.get(y,0) + 1


        for key in s_hashmap.keys():

            if s_hashmap.get(key) != t_hashmap.get(key):
                return False

        return True
