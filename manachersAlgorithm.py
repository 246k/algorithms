def manachersAlgorithm(word):
    n = len(word)
    maxLength = 0
    left = 0
    right = 0
    longestPalindromeArray = [0] * n
    start = 0

    for i in range(n):
        if(i > right):
            k = 1
        else:
            k = min(longestPalindromeArray[left + right - i] // 2, right - i + 1)

        while (
            i - k >= 0
            and i + k < n
            and word[k + i] == word[i - k]
        ):
            k += 1

        longestPalindromeArray[i] = 2 * k - 1

        if i + k - 1 > right:
            left = i - k + 1
            right = i + k - 1

        if maxLength < longestPalindromeArray[i]:
            maxLength = longestPalindromeArray[i]
            start = i

    result = word[start - maxLength // 2 : start + maxLength // 2 + 1]
    if len(result) > 1:
        return result
    else: 
        return "No palindromic substrings found." 