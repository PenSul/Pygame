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

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

class LinkedListNode:
    def __init__(self, key):
        self.val = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, key):
        new_node = LinkedListNode(key)
        new_node.next = self.head
        self.head = new_node

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

# Test cases for generate
class TestGenerate(unittest.TestCase):
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

    def test_data_structure_time(self):
        # Generate a larger dataset of words
        words_copy = ["WORD" + str(i) for i in range(1000000)]  # Generate 1,000,000 words

        # Measure the time taken to initialize the status of each word using hash table lookup
        start_time = time.time()
        # Initialize the status of each word using hash table lookup
        word_status_hash = {word: False for word in words_copy}
        end_time = time.time()
        time_hash_table = end_time - start_time

        # Measure the time taken to initialize the status of each word using BST
        start_time = time.time()
        # Initialize the status of each word using BST
        for word in words_copy:
            BST().root = BST().insert(BST().root, word)
        end_time = time.time()
        time_bst = end_time - start_time
        # Compare the time taken
        self.assertLess(time_hash_table, time_bst)

        # Measure the time taken to initialize the status of each word using linked list
        start_time = time.time()
        # Initialize the status of each word using linked list
        for word in words_copy:
            LinkedList().push(word)
        end_time = time.time()
        time_linked_list = end_time - start_time
        # Compare the time taken
        self.assertLess(time_hash_table, time_linked_list)

        # Measure the time taken to initialize the status of each word using trie
        start_time = time.time()
        # Initialize the status of each word using trie
        for word in words_copy:
            current_node = Trie().root
            for char in word:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            current_node.is_end_of_word = True
        end_time = time.time()
        time_tries = end_time - start_time
        # Compare the time taken
        self.assertLess(time_hash_table, time_tries)

if __name__ == '__main__':
    unittest.main()