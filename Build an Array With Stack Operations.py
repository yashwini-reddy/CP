def buildArray(self, target: List[int], n: int) -> List[str]:
    res=[]
    t=[]
    for i in range(1,n+1):
        if i in target:
            res.append('Push')
            t.append(i)
        else:
            res.append('Push')
            res.append('Pop')
        if target==t:

            return res
        
