# Final code UI
# Kit Horeczy 101189904
# Stephanie Sarria 101216262
# Aditi Manjunath Keertani 101202033

# Imports
# P1
from T008_P5_load_data import book_category_dictionary
# P2
from T008_P2_add_remove_search_dataset import add_book
from T008_P2_add_remove_search_dataset import remove_book
from T008_P2_add_remove_search_dataset import get_books_by_title
from T008_P2_add_remove_search_dataset import get_books_by_rate
from T008_P2_add_remove_search_dataset import get_books_by_category
from T008_P2_add_remove_search_dataset import get_books_by_author
from T008_P2_add_remove_search_dataset import get_books_by_publisher
from T008_P2_add_remove_search_dataset import get_all_categories_for_book_title
# P3
from T008_P3_sorting_fun import category_change
from T008_P3_sorting_fun import sort_books_title
from T008_P3_sorting_fun import sort_books_publisher
from T008_P3_sorting_fun import sort_books_author
from T008_P3_sorting_fun import sort_books_ascending_rate

# Functions
# Add, Remove, GCT functions
def add_book_UI(loaded_dictionary:dict)-> dict:
    """
    Aditi Manjunath Keertani
    This function calls the add book function and uses the input entered by the
    user into the user interface, to return a dictionary with the book added in it.    
    """
    tp = input("Please type the name of the book you wish to add, along with all of its information: ")
    tp = tp.split(',')
    tp2 = tuple(tp)
    add_book(loaded_dictionary, tp2)
    print(loaded_dictionary)

def remove_book_UI(loaded_dictionary:dict)->dict:
    """
    Aditi Manjunath Keertani
    This function calls the add book function and uses the input entered by the 
    user into the user interface, to return a dictionary with the book added in 
    it.
    """
    titlebook = input("Please type the name of the book you wish to remove: ")
    categorybook = input("Please type the category that the book belongs to: ")
    remove_book(loaded_dictionary, titlebook, categorybook)
    print(remove_book)

def get_all_categories_for_book_title_UI(loaded_dictionary):
    """
    Stephanie Sarria
    Prints all categories a book belongs to given input title
    """
    book = input("Select a book: ")
    get_all_categories_for_book_title(loaded_dictionary, book)

# Getting functions
# T)itle   R)ate   A)uthor   P)ublisher   C)ategory
def get_books_by_title_UI(loaded_dictionary:dict)->bool:
    """
    Aditi Manjunath Keertani
    This function calls the get book by title function, and uses the input 
    entered by the user into the user interface to search for a book using its 
    title and return whether the book was found or not.
    """
    titlenameofbook = input("Please type the name of the book you wish to search for: ")
    get_books_by_title(loaded_dictionary, titlenameofbook)
   
def get_books_by_rate_UI(loaded_dictionary:dict)->int:
    """
    Aditi Manjunath Keertani
    This function calls the get book by rate function, and uses the input 
    entered by the user into the user interface to search for a book using its 
    rating and return whether the book was found or not.
    """
    ratingneeded = float(input("Please type the rating of the book you wish to search for: "))
    ratingneeded = int(ratingneeded)
    get_books_by_rate(loaded_dictionary, ratingneeded)

def get_books_by_author_UI(loaded_dicitonary):
    """
    Stephanie Sarria
    Prints all books written by the author given by input
    """
    author_name = input("Enter an author: ")
    get_books_by_author(loaded_dicitonary, author_name)

def get_books_by_publisher_UI(loaded_dicitonary):
    """
    Stephanie Sarria
    Prints books published by the company given by input
    """
    publisher = input("Enter a publisher: ")
    book_category_dictionary(loaded_dicitonary, publisher)
    
def get_books_by_category_UI(loaded_dictionary):
    """
    Stephanie Sarria
    Prints all books in a category, given category input
    """
    category = input("Enter a category: ")
    get_books_by_category(loaded_dictionary, category)

# Sorting functions
# T)itle   R)ate   P)ublisher   A)uthor
def sort_books_title_ui(dictionary: dict):
    """
    Kit Horeczy
    Returns a list of books sorted by title
    """
    print("Your books sorted by title: ")
    print(sort_books_title(dictionary))

def sort_books_ascending_rate_ui(dictionary: dict):
    """
    Kit Horeczy
    Returns a list of books sorted by rate first and then by title if
    rates match
    """
    print("Your books sorted by rate: ")
    print(sort_books_ascending_rate(dictionary))
    
def sort_books_publisher_ui(dictionary: dict):
    """
    Kit Horeczy
    Returns a list of books sorted by publisher first and then by title if
    publishers match
    """
    print("Your books sorted by publisher: ")
    print(sort_books_publisher(dictionary))
    
def sort_books_author_ui(dictionary: dict):
    """
    Kit Horeczy
    Returns a list of books sorted by author first and then by title if authors
    match
    """
    print("Your books sorted by author: ")
    print(sort_books_author(dictionary))

# Display and input functions
def print_display(number:int):
    """
    Kit Horeczy
    Prints a menu given the number that represents the menu
    """
    if number == 1:
        # First inputs
        print('The available commands are:','\n',
              '   L)oad data','\n',
              '   A)dd book','\n',
              '   R)emove book','\n',
              '   G)et book','\n',
              '      T)itle   R)ate   A)uthor   P)ublisher   C)ategory','\n',
              '   GCT) Get all Categories for book Title', '\n',
              '   S)ort books','\n',
              '      T)itle   R)ate   P)ublisher   A)uthor','\n',
              '   Q)uit')
    if number == 2:
        # Sort inputs
        print('The available commands are:','\n',
              'T)itle','\n',
              'R)ate','\n',
              'P)ublisher','\n',
              'A)uthor')
    if number == 3:
        # Get inputs
        print('The available commands are:','\n',
              'T)itle', '\n',
              'R)ate', '\n',
              'A)uthor', '\n',
              'P)ublisher', '\n',
              'C)ategory')
    
def take_input(num:int)->str:
    """
    Kit Horeczy
    Returns desired command by printing menu and creating input request given 
    the number attributed to the the desired menu.
    """
    print_display(num)
    command = input("Please type your command: ")
    return command

# Main function
def load_and_display()-> dict:
    """
    Kit Horeczy
    Stephanie Sarria
    Aditi Manjunath Keertani
    Prints the menu options, requests input from user and calls the appropriate 
    funciton.
    """
    # List initiation
    list_of_options1 = ['L','A','R','G','GCT','S','Q']
    list_of_options_s = ['T','R','P','A']
    list_of_options_g = ['T','R','A','P','C']
    command = take_input(1)                                                     # Input for command
    while command.upper() != 'Q':                                               # Quits with a q or Q input
        if command.upper() in list_of_options1:                                 # Ensure valid option was chosen
            if command.upper() == 'L':                                          # If Load is chosen
                filename = input('What is the name of the csv you would like to use? ')
                loaded_dictionary = book_category_dictionary(filename)
                load = 1
                print(loaded_dictionary)
                command = take_input(1)
                if command.upper() == 'S':                                      # If Sort is chosen after loading
                    command = take_input(2)                                     # Take input
                    if command.upper() in list_of_options_s:                    # Ensure valid option was chosen
                        if command.upper() == 'T':                              # If Title was chosen
                            sort_books_title_ui(loaded_dictionary)
                            command = take_input(1)
                        if command.upper() == 'R':                              # If Rate was chosen
                            sort_books_ascending_rate_ui(loaded_dictionary)
                            command = take_input(1)
                        if command.upper() == 'P':                              # If Publisher was chosen
                            sort_books_publisher_ui(loaded_dictionary)
                            command = take_input(1)
                        if command.upper() == 'A':                              # If Author was chosen
                            sort_books_author_ui(loaded_dictionary)
                            command = take_input(1)
                elif command.upper() == 'G':                                    # If Get is chosen after loading
                    command = take_input(3)
                    if command.upper() in list_of_options_g:
                        if command.upper() == 'T':                              # If Title was chosen
                            get_books_by_title_UI(loaded_dictionary)
                            command = take_input(1)
                        if command.upper() == 'R':                              # If Rate was chosen
                            get_books_by_rate_UI(loaded_dictionary)
                            command = take_input(1)
                        if command.upper() == 'A':                              # If Author was chosen
                            get_books_by_author_UI(loaded_dictionary)
                            command = take_input(1)
                        if command.upper() == 'P':                              # If Publisher was chosen
                            get_books_by_publisher_UI(loaded_dictionary)
                            command = take_input(1)
                        if command.upper() == 'C':                              # If Category was chosen
                            get_books_by_category_UI(loaded_dictionary)
                            command = take_input(1)
                elif command.upper() == 'A':                                    # If Add is chosen after loading
                    add_book_UI(loaded_dictionary)
                    command = take_input(1)
                elif command.upper() == 'R':                                    # If Remove is chosen after loading
                    remove_book_UI(loaded_dictionary)
                    command = take_input(1)
                elif command.upper() == 'GCT':                                  # If GCT is chosen after loading
                    get_all_categories_for_book_title_UI(loaded_dictionary)
                    command = take_input(1)
            else:
                print("File not loaded")
                command = take_input(1)
        else:                                                                   # If command not a valid option
            print("This command does not exist")
            command = take_input(1)
load_and_display()
