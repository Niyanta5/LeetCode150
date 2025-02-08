def is_palindrome(s):
    return s == s[::-1]


def find_subpalindromes(s):
    n = len(s)
    palindromes = []

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]

            if is_palindrome(substring):
                palindromes.append(substring)

    return palindromes


s = "abac"
print(find_subpalindromes(s))
