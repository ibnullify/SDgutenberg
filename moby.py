from functools import reduce

s = []
with open("moby_dick.txt", "rb") as f:
    for i in f.readlines():
        i = i.rstrip('\r\n')
        if (i != ""):
            s.append(i)


t = [x for i in s for x in i.split(" ")]
t.sort()
print t

def single(f, word):
    return reduce( (lambda x, y: 1 if True), f)

print single(t, 'who')
