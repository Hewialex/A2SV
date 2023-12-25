class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        top = 0
        while top + 1 < n and arr[top] < arr[top + 1]:
            top += 1

        if top == 0 or top == n - 1:
            return False

        while top + 1 < n and arr[top] > arr[top + 1]:
            top += 1
        
        return top == n-1