class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''n=len(temperatures)
        res = [0] * n
        for i in range(n):
            for j in range(i+1,n):
                if temperatures[j] > temperatures[i]:
                    ind = j-i
                    res[i] = ind
                    break
        return res 
            ^
        TLE |'''
        n = len(temperatures)
        res = [0] * n
        stack = [] 
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)

        return res



