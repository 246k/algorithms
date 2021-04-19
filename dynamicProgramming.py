def dynamicProgramming(word):
    n = len(word)
    table = [[0 for x in range(n)] for y in range(n)]
    
    max = 1
    i = 0

    while(i<n):
        table[i][i] = True
        i += 1

    start = 0
    i=0
    while i<n-1:
        if(word[i] == word[i+1]):
            table[i][i+1] = True
            start = i
            max = 2
        i+=1

    k=3
    while k<= n:
        i = 0
        while i<(n-k+1):
            j = i+k-1
            if(table[i+1][j-1] and word[i]==word[j]):
                table[i][j] = True

                if(k > max):
                    start = i
                    max = k

            i+=1
        k+=1
    if(max>1):
        return word[start:start+max]
    else:
        return "No palindromic substrings found." 


result = dynamicProgramming("racecarcc")
print(result)