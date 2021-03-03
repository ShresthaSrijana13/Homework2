# Srijana Shrestha
# 1918305

word = input()
forward = ''
backward = ''

for letter in range(len(word)):

    if word[letter].isalpha():

        forward += word[letter].lower()
        backward = word[letter].lower() + backward

if forward == backward:

    print(word + 'is a palindrome')

else:

    print(word + 'is not a palindrome')
