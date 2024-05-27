class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [asteroids[0]]
        for i in asteroids[1:]:
            if i < 0: # asteroid is negative
                destroyed = False
                while stack and abs(i) >= stack[-1]:
                    if stack[-1] < 0: 
                        stack.append(i)
                        break
                    if abs(i) == stack[-1]: 
                        stack.pop()
                        destroyed = True
                        break
                    else:
                        stack.pop()
                if not destroyed and not stack: stack.append(i)
            else: stack.append(i)
        return stack
        