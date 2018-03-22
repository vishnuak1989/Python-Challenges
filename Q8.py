words = input("Enter comma separated words for sorting \n")
words_list = []
words_list = words.split(',')
words_list.sort()
print(','.join(words_list))