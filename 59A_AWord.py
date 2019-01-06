alphabet = "abcdefghijklmnopqrstuvwxyz"
word = input()
if sum([c in alphabet for c in word]) < (len(word)+1) / 2:
    print(word.upper())
else:
    print(word.lower())