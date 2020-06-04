import math
print(dir(math))
msg = "454"
for m in msg:
    print(m)
print(msg)

s = "Python_version_3.8"
for t in zip(s):
    print(t)

w = {"house": "Haus", "cat": "", "red": "rot"}
items_view = w.keys()
items = list(items_view)
print(items)
print(items_view)

# create a 2d array having 0 with column len_w2 and row of len_w1
len_w1 = 5
len_w2 = 6
dp = [[0 for _ in range(len_w2)] for _ in range(len_w1)]
