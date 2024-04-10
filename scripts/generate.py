# Python Module(s)
import random

# Function to generate a list of words from a file
def generate_word_list():
    with open("words.txt", "r") as file:
        return [line.rstrip() for line in file]

# Function to check if a word can be placed in a certain position on the grid
def check_possibility(matrix, word, index, fitting_orders, fitting_order):
    x, y = index
    ix, iy = fitting_orders[fitting_order]
    try:
        for i in range(len(word)):
            if 0 <= y <= 14 and 0 <= x <= 14:
                if matrix[y][x] != "0":
                    return False
                x += ix
                y += iy
            else:
                return False
    except IndexError:
        return False
    return True

# Function to place a word in the grid
def put_in_word(matrix, word, index, fitting_orders, fitting_order):
    x, y = index
    ix, iy = fitting_orders[fitting_order]
    for _ in range(len(word)):
        matrix[y][x] = word[_]
        y += iy
        x += ix

# Function to generate a list of random words
def generate_words(words):
    for i in range(10):
        random_word = random.choice(lst_words)
        words.append(random_word)
        lst_words.remove(random_word)
    return words

# Initialize the grid and alphabet
grid = []
alphabet = "ABCDFEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = list(alphabet)
for i in range(15):
    grid.append(list("0" * 15))

# Generate the list of words and a copy of it
lst_words = generate_word_list()
words = generate_words([])
words_copy = words[::]

# Define the possible movement directions and moves
possibilities = {"f": (1, 0), "b": (-1, 0), "u": (0, -1), "d": (0, 1)}
moves = ["f", "b", "u", "d"]

# Initialize the status of each word with Hash Table
word_status = {}
for word in words_copy:
    word_status[word] = False

# Place the words in the grid
while True:
    if words == []:
        break
    word = random.choice(words)
    words.remove(word)
    x_coordinate = random.randint(0, 14)
    y_coordinate = random.randint(0, 14)
    index = (x_coordinate, y_coordinate)
    pattern = random.choice(moves)
    while not check_possibility(grid, word, index, possibilities, pattern):
        x_coordinate = random.randint(0, 14)
        y_coordinate = random.randint(0, 14)
        index = (x_coordinate, y_coordinate)
    put_in_word(grid, word, index, possibilities, pattern)
    word_status[word] = True

# Fill the empty spaces in the grid with random alphabets
for i in range(15):
    for j in range(15):
        if grid[i][j] == "0":
            grid[i][j] = random.choice(alphabet)