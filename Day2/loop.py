line = input("Enter your fav line")
letters = {}

for ch in line:

    if ch in letters:
        letters[ch]=letters[ch] + 1
    else:
        letters[ch]= 1

print(letters)
# print(letters["a"])