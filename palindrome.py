def isPalindrome(string):
    newString = ''.join(reversed(string))
    if( newString == string ):
        return True
    return False

print(isPalindrome('racecar'))

# Palindrome 
# using reversed()
# def isPalinrome(s):
#     lower = s.lower()
#     newS = ''.join(reversed(lower))
#     if ( lower == newS):
#         return True
#     return False

# print(isPalinrome('AaBaA'))




# def reverse(s):
#     return s[::-1]

# def isPalindrome(s):
#     # calling reverse function
#     rev = reverse(s)

#     # checking if both string are equal or not
#     if (s == rev):
#         return True
#     return False

# print(isPalindrome('daax'))


# # function to check string is 
# # palindrome or not 
# def isPalindrome(str):
 
#     # Run loop from 0 to len/2 
#     for i in xrange(0, len(str)/2): 
#         if str[i] != str[len(str)-i-1]:
#             return False
#     return True
 
# # main function
# s = "malayalam"
# ans = isPalindrome(s)
 
# if (ans):
#     print("Yes")
# else:
#     print("No")


# # function to check string is 
# # palindrome or not
# def isPalindrome(s):
     
#     # Using predefined function to 
#     # reverse to string print(s)
#     rev = ''.join(reversed(s))
 
#     # Checking if both string are 
#     # equal or not
#     if (s == rev):
#         return True
#     return False
 
# # main function
# s = "malayalam"
# ans = isPalindrome(s)
 
# if (ans):
#     print("Yes")
# else:
#     print("No")



# # function which return reverse of a string
# def reverse(s):
#     return s[::-1]
 
# def isPalindrome(s):
#     # Calling reverse function
#     rev = reverse(s)
 
#     # Checking if both string are equal or not
#     if (s == rev):
#         return True
#     return False
 
 
# # Driver code
# s = "racecar"
# ans = isPalindrome(s)
 
# if ans == 1:
#     print("Yes")
# else:
#     print("No")