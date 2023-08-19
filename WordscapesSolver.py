import itertools
import nltk

nltk.download('words')
from nltk.corpus import words

class WordscapesSolver:
    def __init__(self):
        self.word_list = set(words.words())
    
    def generate_solutions(self, letters, min_length=3):
        valid_combinations = {}

        for length in range(min_length, len(letters) + 1):
            valid_words = set()
            for perm in itertools.permutations(letters, length):
                word = ''.join(perm).lower()
                if word in self.word_list:
                    valid_words.add(word)

            if valid_words:
                valid_combinations[length] = valid_words

        return valid_combinations

    def format_output(self, valid_combinations):
        output_string = ""

        for length, words in valid_combinations.items():
            sorted_words = sorted(words)
            output_string += f"Words of length {length}:\n"
            for word in sorted_words:
                output_string += f"{word}\n"
            output_string += "\n"

        return output_string
