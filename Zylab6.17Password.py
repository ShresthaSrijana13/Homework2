# Srijana Shrestha
# 1918305
word = input()

for x in word:
    word = word.replace('i', '1')
    word = word.replace('m', 'M')
    word = word.replace('a', '@')
    word = word.replace('s', '$')
    word = word.replace('o', '.')

print(word+'q*s')
