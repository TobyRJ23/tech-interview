"""A module for the game of scrabble"""

import random

letter_scores = {
  "E": 1, "A": 1, "I": 1, "O": 1,
  "N": 1, "R": 1, "T": 1, "L": 1,
  "S": 1, "U": 1, "D": 2, "G": 2,
  "B": 3, "C": 3, "M": 3, "P": 3,
  "F": 4, "H": 4, "V": 4, "W": 4,
  "Y": 4, "K": 5, "J": 8, "X": 8.,
  "Q": 10, "Z": 10
}

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def calculate_word_score(word: str) -> int:
    """A function that will take a word and calculate the total score"""
    score_count = 0
    for letter in word:
        score_count += letter_scores[letter]
    return score_count


def generate_player_rack() -> list:
    """A function that generates a rack of 7 letters for the player"""
    player_rack = []
    for i in range(7):
        letter_num = random.randint(0, 25)
        player_rack.append(letters[letter_num])
    return player_rack