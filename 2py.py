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

#LEET28

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if needle==haystack[i:len(needle)]:
                return i
        else:
            return -1

        
