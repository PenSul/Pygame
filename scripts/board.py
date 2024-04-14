# Python Module(s)
import pygame
import sys

# Scripts will be loaded here
import generate  
from generate import words_copy  

pygame.init()  # Initialize the pygame module
pygame.display.init()  # Initialize the display
screen = pygame.display.set_mode((1000, 600))  # Set up the display screen with dimensions 800x600 pixels
selected = []  # Initialize an empty list named selected

# Function to display the game over screen
def game_over_screen(screen, list_copy):
    game_over_format = pygame.font.Font("freesansbold.ttf", 100)  # Set the font style and size for the game over message

    if list_copy == []:
        screen.fill((255, 255, 255))  # Fill the screen with white color
        display_word = game_over_format.render("YOU WIN!!!!", True, "Green")  # Render the "YOU WIN" message in green color
        screen.blit(display_word, (175, 200))  # Display the message on the screen at specified coordinates
        # Play the You Win Sound once u win
        pygame.mixer.Sound('assets/sfx/You_Win.wav').play(0)

# Function to remove duplicates from words in a list
def refine_list(lst):
    for i in range(len(lst)):
        lst[i] = remove_duplicate(lst[i])  # Call the remove_duplicate function for each word in the list
    return lst

# Function to remove consecutive duplicate characters from a word
def remove_duplicate(word):
    try:
        s = ""
        s += word[0]  # Add the first character of the word to the new string
        for i in range(1, len(word)):
            if word[i] != s[-1]:  # If the current character is different from the last character in the new string
                s += word[i]  # Add the current character to the new string
        return s
    except IndexError:
        return 0  # Return 0 if an empty word is encountered
    
# Function to display the game board and box(Correct:Green---/-->Already Selected:Cyan)
def display_board():
    x_start = 0
    y_start = 0
    for i in range(15):
        for j in range(15):
            if [x_start, y_start] in guessed_indexes:
                pygame.draw.rect(screen, "green", (x_start, y_start, 40, 40), 0)  # Draw a green rectangle
                pygame.draw.rect(screen, "black", (x_start, y_start, 40, 40), 1)  # Draw a black border
            elif [x_start, y_start] in selected:
                pygame.draw.rect(screen, "cyan", (x_start, y_start, 40, 40), 0)  # Draw a cyan rectangle
                pygame.draw.rect(screen, "black", (x_start, y_start, 40, 40), 1)  # Draw a black border
            else:
                pygame.draw.rect(screen, "blue", (x_start, y_start, 40, 40), 1)  # Draw a blue rectangle
            x_start += 40
        x_start = 0
        y_start += 40

# Function to print the search grid on the screen
def print_search():
    y = 25
    search_format = pygame.font.Font("freesansbold.ttf", 30)  # Set the font style and size for the search grid
    for line in generate.grid:
        x = 21
        for i in range(15):
            search_render = search_format.render(line[i].upper(), True, (0, 0, 0))  # Render each character in uppercase
            width = search_render.get_width()
            height = search_render.get_height()
            screen.blit(search_render, (x - width // 2, y - height // 2))  # Display the character at specified coordinates
            x += 40
        y += 40

# Function to display the words on the screen
def display_words():
    x = 625
    y = 80
    word_format = pygame.font.Font("freesansbold.ttf", 25)  # Set the font style and size for the words
    title_words_format = pygame.font.Font("freesansbold.ttf", 35)  # Set the font style and size for the title
    title_words = title_words_format.render("WORDS TO FIND", True, ('black'))  # Render the title "WORDS" in black
    screen.blit(title_words, (x, 25))  # Display the title at specified coordinates
    for word in generate.words_copy:
        display_word = word_format.render(word, True, (0, 0, 0))  # Render each word in black color
        screen.blit(display_word, (x, y))  # Display the word at specified coordinates
        y += 33

# Function to check if the game is completed
def is_game_completed():
    if not words_to_guess or not words_copy:  # If there are no words left to guess or display
        return True  # Return True indicating the game is completed
    return False  # Return False indicating the game is not completed

drag = False  # Initialize a variable drag to False
guessed = []  # Initialize an empty list named guessed
word = ""  # Initialize an empty string named word
running = True  # Initialize a variable running to True
guessed_indexes = []  # Initialize an empty list named guessed_indexes
words_to_guess = refine_list(generate.words_copy[::])  # Refine the list of words to guess

while running:
    
    screen.fill((255, 255, 255))  # Fill the screen with white color

    display_board()  # Call the function to display the game board
    display_words()  # Call the function to display the words
    print_search()  # Call the function to print the search grid

    if is_game_completed():  # Check if the game is completed
        game_over_screen(screen, words_to_guess)  # Call the game over screen function with the remaining words to guess

    # Event Management aka Input control
    for event in pygame.event.get():  # Iterate through each event in the pygame event queue
        if (event.type != pygame.MOUSEBUTTONUP):
            if event.type == pygame.QUIT:  # If the user clicks the close button
                running = False  # Set running to False to exit the game
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                drag = True  # Set drag to True when the mouse button is pressed
                x, y = pygame.mouse.get_pos()  # Get the current mouse position
                if x <= 600:  # Check if the click is within the grid
                    word += generate.grid[(y // 40)][(x // 40)]  # Add the clicked character to the word
            if event.type == pygame.MOUSEMOTION and drag:
                x, y = pygame.mouse.get_pos()  # Get the current mouse position while dragging
                grid_width = len(generate.grid[0]) * 40
                grid_height = len(generate.grid) * 40
                grid_columns = len(generate.grid[0])
                grid_rows = len(generate.grid)
                if x < grid_width and y < grid_height and y // 40 < grid_rows and x // 40 < grid_columns:
                    word += generate.grid[(y // 40)][(x // 40)]  # Add the character to the word while dragging
                    guessed_indexes.append([x // 40 * 40, y // 40 * 40])  # Add the guessed index to the list

        else:
            drag = False  # Set drag to False when the mouse button is released
            if remove_duplicate(word) in words_to_guess:  # Check if the word is in the words to guess
                selected += (guessed_indexes)  # Add the guessed indexes to the selected list
                index = words_to_guess.index(remove_duplicate(word))  # Get the index of the word in words to guess
                words_to_guess.remove(remove_duplicate(word))  # Remove the word from words to guess
                generate.words_copy.pop(index)  # Remove the word from the generated words list
                pygame.mixer.Sound('assets/sfx/Retro_PowerUP_09.wav').play()  # Play the correct sound when a word is found correctly

            word = ""  # Reset the word
            guessed_indexes = []  # Reset the guessed indexes

        pygame.display.update()  # Update the display to show any changes

# I am finally done with this sh*t
# Good Luck playing the game :) Every round take you 5 mins
# Debugging is a pain