import tkniz as nk
import json
import nltk 
import pandas as pd
from collections import defaultdict
dataframe = pd.read_excel('xlsx files/problemStatements.xlsx')
column_name = 'Description'

column_data = dataframe[column_name].tolist()
word_count = defaultdict(int)

for description in column_data:
    words = nk.tknxz(description)
    for word in words:
        word_count[word] += 1

frequent_words = {word: count for word, count in word_count.items()}

sorted_frequent_words = dict(sorted(frequent_words.items(), key=lambda item: item[1]))

file = open("test2.json", "w")
json.dump(sorted_frequent_words,file)
file.close()