#This exercise was conducted with Python 3.6.5

import operator
import re
__author__ = 'codesse'


class AngryWordAnalysis:
    angry_words = []
    headlines = []

    def __init__(self, angrywords='angry_words.txt', headlines='headlines.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.all_headline_scores = {}
        self.leaderboard = []  # initialise an empty leaderboard
        with open(angrywords) as f:
            self.angry_words = f.read().splitlines()

        with open(headlines) as f:
            self.headlines = f.read().splitlines()


    def build_angry_word_leaderboard(self):
        self.get_angry_score()
        self.create_leaderboard(self.all_word_scores)

    def get_angry_score_for_headline(self):
        for headline in self.headlines:
            words = headline.split()
            angry_score = self.return_outrage_score(words)
            self.all_headline_scores.update( { headline: angry_score} )


    def return_outrage_score(self, words):
        total_score = 0
        for word in words:
            if word.lower() in self.angry_words:
                total_score += 1
        return total_score

    
