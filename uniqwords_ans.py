import collections
import string
import sys


def number_of_words(item):
 #   print(item)
  #  print(item[1])
    return item[1]


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1
for word, count in sorted(words.items(), key=number_of_words):
    print("'{0}' occurs {1} times".format(word, count))
#print(words.items())
