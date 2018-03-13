list = input("Input a letter of the alphabet: ")

if list in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % list)
elif list== 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % list) 
