class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        tot = sum(distance)
        d1=0
        if start<destination:
          d1 = sum(distance[start:destination:])
        else:
          d1 = sum(distance[destination:start])
        return min( tot-d1, d1)    