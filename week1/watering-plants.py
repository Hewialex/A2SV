class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        N = len(plants)
        total = 0
        current = capacity

        for i in range(N):
          if plants[i] <= capacity:
            capacity -= plants[i]
            total += 1
          else:
            total += i
            capacity = current
            capacity -= plants[i]
            total += (i+1)
        return total 