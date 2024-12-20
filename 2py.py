#slicing
a="benhur"

b="cur"
def strpresent():
    for i in range(len(a)-len(b)+1):
        if b==a[i:]:
            return i
    else:
        return -1
print(strpresent())

