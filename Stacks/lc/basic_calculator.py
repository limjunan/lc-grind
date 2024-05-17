class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return int(s)
        
        stack = [0, 1, 0] # [res, opr, res, opr, res, opr, res]

        for i in s:
            if i == ' ': continue

            if i.isnumeric():
                stack[-1] = stack[-1] * 10 + int(i)

            if i == '+' or i == '-':
                if stack[-2] == 1: stack[-3] += stack[-1]
                else: stack[-3] -=  stack[-1]

                if i == '+': stack[-2] = 1
                if i == '-': stack[-2] = 0

                stack[-1] = 0

            if i == '(':
                stack.append(1)
                stack.append(0)
                
            if i == ')':
                if stack[-2] == 1: stack[-3] += stack[-1]
                else: stack[-3] -=  stack[-1]
                stack.pop()
                stack.pop()
        
        if len(stack) == 3:
            if stack[1] == 1: stack[0] += stack[2]
            if stack[1] == 0: stack[0] -= stack[2]

        return stack[0]



            

                    
            

        



                

        


