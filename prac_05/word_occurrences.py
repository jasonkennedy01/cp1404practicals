"""
Word Occurences
Estimate: 10mins
Actual: 10mins
"""
from operator import itemgetter

string = input("Text: ")
words = string.split()

word_to_occurrence = {}
for word in words:
    word_to_occurrence[word] = word_to_occurrence.get(word, 0) + 1

longest_word = max((len(word) for word in word_to_occurrence.keys()))

for word in sorted(word_to_occurrence, key=itemgetter(0)):
    print(f"{word:{longest_word}} : {word_to_occurrence[word]}")
