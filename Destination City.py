from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s=defaultdict(int)
        for a,b in paths:
            s[a]+=1
            s[b]+=0
        for x in s.keys():
            if s[x]==0:
                return x
        return ""  
