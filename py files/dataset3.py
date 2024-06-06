import tkniz as tk
import nltk
import pandas as pd
from collections import defaultdict
nltk.download('punkt')
dataframe = pd.read_excel('random.xlsx')
column_name = 'Column 1'

column_data = dataframe[column_name].tolist()
word_count = defaultdict(int)

for description in column_data:
    words = tk.tknxz(description)
    for word in words:
        word_count[word] += 1

frequent_words = {word: count for word, count in word_count.items()}

sorted_frequent_words = dict(sorted(frequent_words.items(), key=lambda item: item[1]))

with open('frequent_words3.txt', 'w') as file:
    for word, count in sorted_frequent_words.items():
        file.write(f"{word}: {count}\n")