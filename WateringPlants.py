class Solution(object):
    def wateringPlants(self, plants, capacity):
        x = -1
        steps = 0
        cap = capacity
        while x != len(plants)-1:
            if x == -1: steps += 1
            x += 1
            if capacity >= plants[x]:
                capacity -= plants[x]
                steps += 1
            elif capacity < plants[x]:
                steps += x+1
                temp = x
                x = -1
                capacity = cap
                x = temp-1
                steps += temp - 1
        return steps-1
