class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0

        stack = []
        poppedList = []
        output = 0
        current = 0

        for i in height:
            #print(stack, output)
            if not stack:
                stack.append(i)
                continue
            if i >= stack[-1] and len(stack) == 1:
                stack.pop()
                stack.append(i)
                continue
            if i < stack[-1]: 
                stack.append(i)
                continue
            else:
                while len(stack) > 1 and stack[-2] >= stack[-1] and i > stack[-1]:
                    popped = stack.pop()
                    if not poppedList or popped >= poppedList[-1]: poppedList.append(popped)
                diff = min(stack[-1], i)
                for p in poppedList:
                    output += diff - p
                    stack.append(diff)
                
                stack.append(i)
                
                poppedList = []
            
        return output