class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second

solution = Solution()
# Call the climbStairs method and print the result
result = solution.climbStairs(10)
print(result)  # Output should be 5

