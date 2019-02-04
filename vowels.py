vowel=["a","e","i","o","u"]
c=input()
if c in vowel:
	print ("Vowel")
elif ((c>='a' and c<='z') or (c>='A' and c<='Z')):
	print("Consonant")
else:
	print ("Invalid")
