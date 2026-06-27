class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) - 1
        max_value = arr[n]
        arr[n] = -1

        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] = max_value

            if temp > max_value:
                max_value = temp
        
        return arr
