class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower()
                for x in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(x, '')
                all_words[file_name] = words.split()
        return all_words

    def find(self, word):
        find_index = {}
        for file_name, words in self.get_all_words().items():
            find_index[file_name] = words.index(word.lower()) + 1
        return find_index

    def count(self, word):
        count_word = {}
        for file_name, words in self.get_all_words().items():
            count_word[file_name] = words.count(word.lower())
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
