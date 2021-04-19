def manachersAlgorithm(word):
    maxLength = 0
    l, r = 0, 0

    longestPalindromeArray = [1 for i in range(len(word))]

    for i in range(len(word)):
        k = 1 if i > r else min(longestPalindromeArray[l + r - i] // 2, r - i + 1)
        while (
            i - k >= 0
            and i + k < len(word)
            and word[k + i] == word[i - k]
        ):
            k += 1

        longestPalindromeArray[i] = 2 * k - 1

        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1

        if maxLength < longestPalindromeArray[i]:
            maxLength = longestPalindromeArray[i]
            start = i

    result = word[start - maxLength // 2 : start + maxLength // 2 + 1]
    if len(result) > 1:
        return result
    else: 
        return "No palindromic substrings found." 


print(manachersAlgorithm("racecarpdfg"))
