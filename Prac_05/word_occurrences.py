count_of_words = {}
user_input = input("Text: ")
words = user_input.split()
for word in words:
    frequency = count_of_words.get(word, 0)
    count_of_words[word] = frequency + 1

words = list(count_of_words.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, count_of_words[word]))