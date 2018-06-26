# a = 1.3
# b = 2.5
# c = a + b
# print (c)

# print('hello world'[::-1])



# '''
#     multiple
#     line comment
# '''

# # If Elif Else
# x = 4

# if x < 6:
#     print('True')
# else:
#     print('false')

# color = 'red'

# if color == 'red':
#     print('yea')
# elif color == 'blue':
#     print('no')
# else:
#     print('purple')

# # Loops
# people = ['John', 'Wick', 'Ann']
# for person in people:
#     print('Hello,', person)

# Function
def sayHi():
    print('Hello World')

sayHi()

def sayHello(name):
    print('Hello,', name)

sayHello('Wick')

def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(2, 3))

# Scoppes
def addOneToNum(num):
    num = num + 1
    print('Inside:', num)
    return

num = 5
addOneToNum(num)

print('Outside:', num)

myStr = "Ayo Ready"
print(myStr.capitalize())

print(myStr.swapcase())

print(myStr.replace('Ready', 'Yessir'))

print(len(myStr))

# Count
sub = 'y'
print(myStr.count(sub))

print(myStr.startswith('Ayo'))

print(myStr.endswith('r'))

print(myStr.split())

print(myStr.find('Ready'))