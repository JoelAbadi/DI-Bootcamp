import string
import re


class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else f"'{word}' not found in text."

    def most_common_word(self):
        words = self.text.lower().split()
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        most_common = max(frequency, key=frequency.get)
        return most_common

    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return cls(content)
        except FileNotFoundError:
            return f"File at '{file_path}' not found."


class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)
        return cleaned_text

    def remove_stop_words(self):
        stop_words = {
            "a", "the", "is", "in", "on", "and", "or", "to", "of", "for", "with", "that", "this", "it", "as", "an", "are", "at", "by"
        }
        words = self.text.lower().split()
        filtered_words = [word for word in words if word not in stop_words]
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return cleaned_text


text_data = "The quick brown fox jumps over the lazy dog! Isn't it amazing? Yes, it is amazing."

# Original analysis
text = Text(text_data)
print(" Word frequency of 'the':", text.word_frequency("the"))
print(" Most common word:", text.most_common_word())
print(" Unique words:", text.unique_words())

# Text modification
mod_text = TextModification(text_data)
print("\n Text without punctuation:\n", mod_text.remove_punctuation())
print("\n Text without stop words:\n", mod_text.remove_stop_words())
print("\n Text without special characters:\n", mod_text.remove_special_characters())
