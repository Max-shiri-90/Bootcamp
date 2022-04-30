num = int(input())
word_set = {}
for i in range(num):
    word = input()
    if word in word_set:
        word_set[word] += 1
    else:
        word_set[word] = 1
print(len(word_set))
for i in word_set:
    print(word_set[i], end=" ")
    
