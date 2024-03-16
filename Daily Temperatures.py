def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    ans=[0]*len(temperatures)
    stack=[]
    for i,temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            index=stack.pop()  
            ans[index]=i-index #differnece
        stack.append(i) #storing the current index in the stack
    return ans
