def manachersAlgorithm(word):
    maxLength = 0
    left = 0
    right = 0
    start = 0
    new_input_string = ""

    for i in word[: len(word) - 1]:
        new_input_string += i + "|"
    # append last character
    new_input_string += word[-1]
    n = len(new_input_string)
    longestPalindromeArray = [0] * n

    for i in range(n):
        if(i > right):
            k = 1
        else:
            k = min(longestPalindromeArray[left + right - i] // 2, right - i + 1)

        while (
            i - k >= 0
            and i + k < n
            and new_input_string[k + i] == new_input_string[i - k]
        ):
            k += 1

        longestPalindromeArray[i] = 2 * k - 1

        if i + k - 1 > right:
            left = i - k + 1
            right = i + k - 1

        if maxLength < longestPalindromeArray[i]:
            maxLength = longestPalindromeArray[i]
            start = i

    result = new_input_string[start - maxLength // 2 : start + maxLength // 2 + 1]
    if len(result) > 1:
        return result.replace('|', '')
    else: 
        return "No palindromic substrings found." 