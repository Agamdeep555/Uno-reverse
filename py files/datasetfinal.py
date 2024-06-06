from collections import defaultdict

def read_text_file(file_path):
    word_count = defaultdict(int)
    with open(file_path, 'r') as file:
        for line in file:
            word, count = line.strip().split(': ')
            word_count[word] = int(count)
    return word_count

file_paths = ['txt files/frequent_words.txt', 'txt files/frequent_words3.txt', 'txt files/frequent_words4.txt', 'txt files/frequent_words5.txt']
all_word_counts = [read_text_file(file_path) for file_path in file_paths]

for word_count in all_word_counts[1:]:
    for word, count in word_count.items():
        all_word_counts[0][word] += count

with open('frequent_words.txt', 'w') as file:
    for word, count in all_word_counts[0].items():
        file.write(f"{word}: {count}\n")
