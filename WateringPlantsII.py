class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        refill = 0
        a = capacityA
        b = capacityB
        for i in range(len(plants)):
            if len(plants)%2 == 0:
                if i == len(plants)//2:
                    break
            j = -(i+1)
            if capacityA >= plants[i] and i != len(plants)//2:
                capacityA -= plants[i]
            elif capacityA < plants[i] and i != len(plants)//2:
                refill += 1
                capacityA = a
                capacityA -= plants[i]
            if capacityB >= plants[j] and i != len(plants)//2:
                capacityB -= plants[j]
            elif capacityB < plants[j] and i != len(plants)//2:
                refill += 1
                capacityB = b
                capacityB -= plants[j]
            if len(plants)%2 != 0 and i == len(plants)//2 and len(plants)!=1:
                if capacityA == capacityB:
                    if capacityA >= plants[i]:
                        capacityA -= plants[i]
                    else:
                        refill += 1
                        capacityA = a
                        capacityA -= plants[i]
                    break
                elif capacityA != capacityB:
                    m = max(capacityA,capacityB)
                    if m >= plants[i]:
                        m -= plants[i]
                    else:
                        refill += 1
                        m = a
                        m -= plants[i]
                    break
        return refill
        
