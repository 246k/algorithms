def manachersAlgorithm(word):
    maxLength = 0
    newInputString = ""
    outputString = ""

    newInputString = word
    # append last character
    newInputString += word[-1]

    # we will store the starting and ending of previous furthest ending palindromic
    # substring
    l, r = 0, 0

    # length[i] shows the length of palindromic substring with center i
    length = [1 for i in range(len(newInputString))]

    # for each character in new_string find corresponding palindromic string
    for i in range(len(newInputString)):
        k = 1 if i > r else min(length[l + r - i] // 2, r - i + 1)
        while (
            i - k >= 0
            and i + k < len(newInputString)
            and newInputString[k + i] == newInputString[i - k]
        ):
            k += 1

        length[i] = 2 * k - 1

        # does this string is ending after the previously explored end (that is r) ?
        # if yes the update the new r to the last index of this
        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1

        # update max_length and start position
        if maxLength < length[i]:
            maxLength = length[i]
            start = i

    # create that string
    s = newInputString[start - maxLength // 2 : start + maxLength // 2 + 1]
    for i in s:
        outputString += i
    if len(outputString) > 1:
        return outputString
    else: 
        return "No palindromic substrings found." 


print(manachersAlgorithm("racecar"))
