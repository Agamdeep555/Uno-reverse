
import tkniz as tk
import nltk
import pandas as pd
from collections import defaultdict
nltk.download('punkt')
dataframe = pd.read_excel('2022 set.xlsx')
column_data = dataframe.iloc[3,:]
print(column_data)
word_count = defaultdict(int)



for description in column_data:
     words = tk.tknxz(description)
     for word in words:
         word_count[word] += 1

frequent_words = {word: count for word, count in word_count.items() if 5<= count <= 100}

sorted_frequent_words = dict(sorted(frequent_words.items(), key=lambda item: item[1]))

with open('frequent_words2.txt', 'w') as file:
     for word, count in sorted_frequent_words.items():
         file.write(f"{word}: {count}\n")