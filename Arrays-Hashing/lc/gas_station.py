# Submitted Solution 1
# Brute force

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for g in range(len(gas)):
            currentGas = 0
            loop = True
            for i in range(len(gas)):
                currentGas += gas[i]
                print(g, i, currentGas)

                if cost[i] > currentGas: 
                    loop = False
                    break
                currentGas -= cost[i]
                

            if loop == True: return g
            gas =  gas[1:] + [gas[0]]
            cost = cost[1:] + [cost[0]]

        return -1
    
# Submitted Solution 2
# Greedy Algotirhm

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        currentGas = 0
        output = -1
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        if sum(diff) < 0: return -1
        
        for i in range(len(diff)):
            currentGas += diff[i]
            if currentGas < 0: 
                currentGas = 0
                output = -1
                continue
            
            if output == -1:
                output = i

        return output
                
            

