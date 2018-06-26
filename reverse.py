# Using Loop
def reverse(s):
    str = ''
    for i in s:
        str = i + str
    return str

print(reverse('hello world'))


# Using reversed()
def reverseStr(string):
    newString = ''.join(reversed(string))
    return newString

print(reverseStr('John Wick'))

# Reverse List
def Reverse(lst):
    lst.reverse()
    return lst
     
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))