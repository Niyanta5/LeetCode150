from typing import List


class Solution:
    def minimumCostToClimbStairs(self, cost: List[int]) -> int:
        first, second = cost[0], cost[1]
        n = len(cost)

        for i in range(2, n):
            current = cost[i] + min(first, second)
            first, second = second, current

        return min(first, second)


solution = Solution()
result = solution.minimumCostToClimbStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(result)
