# 1. Write a program which accepts one character and checks whether it is vowel or consonant.

vowel = ['a', 'e', 'i', 'o', 'u']
word = input("Enter a word: ").lower()

for i in word:
  if i in vowel:
    print("Letter is Vowel: " + i)
  else:
    print("Letter is Consonant: " + i)