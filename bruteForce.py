def bruteForce(word):
    n = len(word)
    maxLength = 1
    start = 0
    isPalindrome = True

    for i in range(n):
        for j in range(i, n):
            isPalindrome = True
            for k in range(0, ((j-i)//2)+1):
                if(word[i+k] != word[j-k]):
                    isPalindrome = False
            if(isPalindrome and ((j-i+1)>maxLength)):
                start = i
                maxLength = j-i+1

    if(maxLength > 1):
        return word[start:start+maxLength]
    else:
        return "No palindromic substrings found."