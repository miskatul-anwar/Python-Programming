list = [1, 2, 1]
list_copy = list.copy()
list_copy.reverse()
if list == list_copy:
    print("Palindrome")
else:
    print("Not Palindrome")
