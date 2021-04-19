# def manachersAlgorithm(word):
#     n = len(word)
#     n = 2*n + 1
#     longestPalindromeArray = [0] * n
#     #longestPalindromeArray[0] = 0
#     #longestPalindromeArray[1] = 1
#     centerIndex = 1
#     rightIndex = 2
#     right = 0
#     iMirror = 0
#     maxLength = 0
#     maxCenter = 0
#     start = -1
#     end = -1
#     diff = -1

#     print(longestPalindromeArray[0], longestPalindromeArray[1])

#     for right in range(1, n-1):
#         iMirror = 2*centerIndex - right
#         longestPalindromeArray[right] = 0
#         diff = rightIndex - right

#         if(diff>0):
#             longestPalindromeArray[right] = min(longestPalindromeArray[iMirror], diff)
#         try:
#             while((right + longestPalindromeArray[right]) < n and \
#                  (right - longestPalindromeArray[right]) > 0 and \
#                      (((right + longestPalindromeArray[right] + 1) % 2 == 0) or \
#                          (word[(right + longestPalindromeArray[right] + 1) / 2] == word[(right - longestPalindromeArray[right] - 1) / 2]))):
#                     # first = (right + longestPalindromeArray[right] + 1) / 2
#                     # second = (right - longestPalindromeArray[right] - 1) / 2
#                     # print("First " + str(first) + " Second " + str(second))
#                     longestPalindromeArray[right]+=1
#         except Exception as e:
#             pass

#         if (int(longestPalindromeArray[right]) > maxLength):
#             maxLength = longestPalindromeArray[right]
#             maxCenter = right

#         if(int(right + longestPalindromeArray[right]) > rightIndex):
#             centerIndex = right
#             rightIndex = right + longestPalindromeArray[right]

#     start = (maxCenter - maxLength) / 2
#     end = start + maxLength - 1
#     print("Start " + str(start) + " End " + str(end))
#     return word[int(start):int(end+1)]

# result = manachersAlgorithm("racecar")
# print(result)