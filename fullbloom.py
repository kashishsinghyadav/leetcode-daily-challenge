
class Solution:
    def fullBloomFlowers(self, flowers, people):
        n = len(flowers)
        start = [0] * n
        end = [0] * n

        # Step 1: Extract the start and end days of flower blooms into separate arrays.
        for i in range(n):
            start[i] = flowers[i][0]
            end[i] = flowers[i][1] + 1  # Adding 1 to mark the end of bloom period.

        # Step 2: Sort both arrays for efficient binary searching.
        start.sort()
        end.sort()

        ans = []

        # Step 3: Iterate through each person's specified day.
        for person in people:
            e = self.binarySearch(end, person)  # Find the rightmost flower end day before or on the person's day.
            s = self.binarySearch(start, person)  # Find the rightmost flower start day before or on the person's day.

            # Step 4: Calculate the answer by subtracting the end count from the start count for each person.
            ans.append(s - e)
        return ans

    # Step 5: Binary search to find the rightmost position of 'target' in the array 'A'.
    def binarySearch(self, A, target):
        l = 0
        r = len(A)
        while l < r:
            mid = (l + r) // 2
            if target < A[mid]:
                r = mid
            else:
                l = mid + 1
        return l
