words=("Apple Banana Orange Banana Orange Apple")
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
print(word_count)