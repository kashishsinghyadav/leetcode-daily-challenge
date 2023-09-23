class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        flips = []

        def find_max(arr, end):
            maxi = max(arr[:end])
            return arr.index(maxi)

        def flip(arr, idx):
            return arr[:idx + 1][::-1] + arr[idx + 1:]

        for end in range(n, 1, -1):
            idx = find_max(arr, end)
            if idx != end - 1:
                if idx != 0:
                    arr = flip(arr, idx)
                    flips.append(idx + 1)
                arr = flip(arr, end - 1)
                flips.append(end)
        return flips
