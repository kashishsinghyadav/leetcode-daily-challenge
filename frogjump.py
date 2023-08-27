class Solution:
    def canCross(self, stones: List[int]) -> bool:
        goal = stones[-1]
        stones = set(stones)

        @cache
        def dp(stone, k):
            if stone == goal:
                return True
            return any(
                dp(stone + nk, nk)
                for nk in (k - 1, k, k + 1)
                if nk > 0
                and stone + nk in stones
            )

        return dp(0, 0)
