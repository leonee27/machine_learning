import numpy as np

a = np.array([[0,1,2,3,4,5],[6,7,8,9,10,11],[12,13,14,15,16,17],[18,19,20,21,22,23],[24,25,26,27,28,29],[30,31,32,33,34,35]])

b = a.reshape(36)
print(b)

print(a[2:4,2:4])

s = 'abcdefghijklmn'


def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    count = 1
    temp = 1
    sub= ""+s[0]
    f = 0

    # for i in range(1, len(s)):


    print(sub)
    print(s[::3])

lengthOfLongestSubstring(s)