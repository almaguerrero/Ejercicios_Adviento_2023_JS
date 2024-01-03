def palin(word):
    word_2 = word[::-1]
    if(word_2 == word):return True

print(palin("radar"))