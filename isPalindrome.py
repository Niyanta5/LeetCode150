class Solution:
    def isPalindrome(self, x:int) -> bool:
        x = str(x)
        if x == x[::-1]:
            return True
        return False

    def main(self):
        arr = [12321]
        result = self.isPalindrome(arr[0])
        print(result)

solution = Solution()
solution.main()
