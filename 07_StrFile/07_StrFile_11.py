word = input()
vowels = ['a', 'e', 'i', 'o', 'u']
if (word[-1] == 'x' or word[-1] == 's' or word[-2:] == 'ch'):
    word += 'es'
elif word[-1] == 'y' and word[-2] not in vowels:
    word = word[:-1] + 'i'
    word += 'es'
else:
    word += 's'
print(word)
