class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            distanceToTarget = abs(target[0]-ghost[0]) + abs(target[1]-ghost[1])

            if distanceToTarget <= d:
                return False
        return True