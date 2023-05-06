'''
(a) i es 3, j es 5, y k es 7
(b) i es 3, j es 7, y k es 5
(c) i es 5, j es 3, y k es 7
(d) i es 5, j es 7, y k es 3
(e) i es 7, j es 3, y k es 5
(f) i es 7, j es 5, y k es 3
'''
i = 7
j = 5
k = 3

# i, j, and k are numbers
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i =", i, " j =", j, " k =", k)
