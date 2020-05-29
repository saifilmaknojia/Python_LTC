import math
print(dir(math))
msg = "454657"
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
