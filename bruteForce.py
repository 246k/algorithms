def bruteForce(word):
    n = len(word)
    isPalindrome = True
    max = 1
    start = 0

    for i in range(n):
        for j in range(i, n):
            isPalindrome = True
        for k in range(0, ((j-i)//2)+1):
            if(word[i+k] != word[j-k]):
                isPalindrome = False
        if(isPalindrome and (((j-i)+1)>max)):
            start = i
            max = j-i+1

    if(max>1):
        return word[start:max]
    else:
        return "No palindromic substrings found."