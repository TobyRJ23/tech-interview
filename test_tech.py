"""A module to test scrabble board function"""
# Assign seven tiles chosen randomly from the English alphabet to a player's rack.

from tech_main import Calculate_word_score, letter_scores, Generate_player_rack

def test_word_score_returns_int():
    """test to check if calculate word is an int"""
    score = Calculate_word_score('TOBY')
    assert isinstance(score, int) == True

def test_word_score_total_correct():
    """test to see if the word score is correct"""
    score = Calculate_word_score('TOBY') 
    assert score == 9

def test_for_empty_string():
    """test to see if score is zero for empty string"""
    score = Calculate_word_score('') 
    assert score == 0

def test_letter_scores():
    """test to see if letter scores is dictionary and contains all letters"""
    assert isinstance(letter_scores, dict) == True
    assert len(letter_scores) == 26

def test_size_of_player_rack():
    """Test to see if the player rack generated is 7"""
    assert len(Generate_player_rack()) == 7

def test_to_check_elements_are_in_letter_score():
    """test to see that elements are in letter score"""
    player_rack = Generate_player_rack()
    for letter in player_rack:
        assert letter in letter_scores