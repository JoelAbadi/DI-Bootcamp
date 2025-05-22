# anagram_checker.py

class AnagramChecker:
    def __init__(self, wordlist_path):
        with open(wordlist_path, 'r') as file:
            self.wordlist = [word.strip().lower() for word in file.readlines()]

    def is_valid_word(self, word):
        return word.lower() in self.wordlist

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()

    def get_anagrams(self, word):
        return [w for w in self.wordlist if self.is_anagram(word, w)]
