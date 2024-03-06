def ispalindrome(string):
    return string == ''.join(reversed(string))
string = input("Enter a string: ")
if ispalindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")