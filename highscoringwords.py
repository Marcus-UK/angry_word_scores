import operator
__author__ = 'codesse'


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.all_word_scores = {}
        self.leaderboard = []  # initialise an empty leaderboard
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return:
        """

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return:
        """

    def get_word_scores(self):
        for word in self.valid_words:
            if len(word) >= self.MIN_WORD_LENGTH:
                word_letters = list(word)
                word_score = self.combine_letter_scores(word_letters)
                self.all_word_scores.update( { word: word_score} )

    def combine_letter_scores(self, letters):
        total_score = 0
        for letter in letters:
            letter_score = self.letter_values.get(letter, 0 )
            total_score += letter_score
        return total_score

    def create_top_100_list(self):
        top_one_hundred = sorted(self.all_word_scores.items(), key=operator.itemgetter(1), reverse=True)[:self.MAX_LEADERBOARD_LENGTH]
        for word, score in top_one_hundred:
            self.leaderboard.append(word)
