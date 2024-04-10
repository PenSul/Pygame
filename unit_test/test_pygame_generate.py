'''Pygame/Generate Tests'''

# Python Module(s)
import os
import sys
import unittest
import time
from unittest.mock import patch

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.generate import check_possibility, put_in_word, generate_word_list, generate_words, words_copy

class TestWordPuzzle(unittest.TestCase):

    def test_generate_word_list(self):
        # Test if generate_word_list returns a list of words
        words = generate_word_list()
        self.assertIsInstance(words, list)
        for word in words:
            self.assertIsInstance(word, str)

    def test_check_possibility(self):
        # Test the check_possibility function with different scenarios
        matrix = [['0'] * 15 for _ in range(15)]
        word = "TEST"
        index = (5, 5)
        fitting_orders = {"f": (1, 0)}
        fitting_order = "f"
        self.assertTrue(check_possibility(matrix, word, index, fitting_orders, fitting_order))

    def test_put_in_word(self):
        # Test the put_in_word function by checking if the word is correctly placed in the matrix
        matrix = [['0'] * 15 for _ in range(15)]
        word = "TEST"
        index = (5, 5)
        fitting_orders = {"f": (1, 0)}
        fitting_order = "f"
        put_in_word(matrix, word, index, fitting_orders, fitting_order)
        self.assertEqual(matrix[5][5], 'T')
        self.assertEqual(matrix[5][6], 'E')
        self.assertEqual(matrix[5][7], 'S')
        self.assertEqual(matrix[5][8], 'T')

    def test_generate_words(self):
        # Test if generate_words generates a list of random words
        words = generate_words([])
        self.assertIsInstance(words, list)
        for word in words:
            self.assertIsInstance(word, str)

    def test_initialize_word_status_speed_comparison(self):
        # Generate a larger dataset of words
        words_copy = ["WORD" + str(i) for i in range(1000000)]  # Generate 1,000,000 words

        # Measure the time taken to initialize the status of each word using linear search
        start_time = time.time()
        # Initialize the status of each word using linear search
        word_status = {}
        for word in words_copy:
            word_status[word] = False
        end_time = time.time()
        time_linear_search = end_time - start_time

        # Measure the time taken to initialize the status of each word using hash table lookup
        start_time = time.time()
        # Initialize the status of each word using hash table lookup
        word_status_hash = {word: False for word in words_copy}
        end_time = time.time()
        time_hash_table = end_time - start_time

        # Compare the time taken with and without the hash table
        self.assertLess(time_hash_table, time_linear_search)

if __name__ == '__main__':
    unittest.main()