n= input('Enter any number : ')
try:
    val = int(n)
    if n== str(n)[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is not a palindrome')
except ValueError:
    print("That's not a valid number, Try Again !")
