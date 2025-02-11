# Kit Horeczy 101189904
# Stephanie Sarria 101216262
# Aditi Manjunath Keertani 101202033

# imports
from T008_P5_load_data import book_category_dictionary
from unit_testing import check_equal

# Refactoring Code
def category_change(input_dict:dict)->list:
    """
    Kit Horeczy 101189904
    Returns a list of books with categories attributed to the category key as a
    list, given a dictionary of categories, when each category has a book
    dictionaries attributed to it.
    """
    # List initiation:
    past_book_title = []
    list_of_sep_books = []
    category_add = []
    final_list = []
    prev_books = []
    past_book_title = []
    #adds all books to a list and adds the category to the book dictionary
    for category in input_dict.items():
        for book in category[1]:
            book.update({'category':category[0]})
            list_of_sep_books.append(book)
    #length of list of books
    length = (len(list_of_sep_books))
    #updates categories of each book to include all categories for that title
    for book1 in list_of_sep_books:
        if book1['title'] not in past_book_title:
            category_add = []
            category_add.append(book1['category'])
            for book2 in list_of_sep_books:
                if book1['title']==book2['title']:
                    if book1['category']!= book2['category']:
                        category_add.append(book2['category'])
                        book1.update({'category':category_add})
            past_book_title.append(book1['title'])
    #removes repeat books
    for dictionary in list_of_sep_books:
        if dictionary.get('title') not in prev_books:
            prev_books.append(dictionary.get('title'))
            final_list.append(dictionary)
    return final_list

# Dictionaries for doc string samples
dictionary_ex = {'Cat1':[{'title': "D", 'author': 'E', 'rating': 3.6, 'publisher': 'H', 'pages': 323, 'language': 'English'},
                       {'title': "A", 'author': 'B', 'rating': 3.9, 'publisher': 'F', 'pages': 400, 'language': 'English'}],
              'Cat2': [{'title': 'I', 'author': 'J', 'rating': 5.0, 'publisher': 'C', 'pages': 200, 'language': 'English'},
                       {'title': 'G', 'author': 'B', 'rating': 4.3, 'publisher': 'K', 'pages': 183, 'language': 'English'},
                       {'title': "D", 'author': 'E', 'rating': 3.6, 'publisher': 'H', 'pages': 323, 'language': 'English'}]}
sample_dictionary = {'CategoryA': [{'title': "Drew", 'author': 'Veronica', 'rating': 3.6, 'publisher': 'Hamlitlon', 'pages': 323, 'language': 'English'},
                                   {'title': "Pal", 'author': 'Ren', 'rating': "N/A", 'publisher': 'Herbert', 'pages': 100, 'language': 'English'}],
                     'CategoryB': [{'title': "Drew", 'author': 'Ron', 'rating': 4.3, 'publisher': 'Landon', 'pages': 300, 'language': 'English'},
                                   {'title': "Rain", 'author': 'Paul', 'rating': 3.6, 'publisher': 'H', 'pages': 323, 'language': 'English'}]}
# Dictionaries for main script tests
minidictionary1 = {'Legal': [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham',
                              'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'language': 'English'}],
                   'Investing':[{'title': 'Rich Dad Poor Dad', 'author': 'Robert Kiyosaki', 'rating': 4.7, 'publisher': 'Warner Books', 'pages': 366,
                                 'language': 'English'}],
                   'Information Technology': [{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader',
                                               'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'language': 'English'}],
                   'Horror': [{'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 
                               'pages': 208, 'language': 'English'}]}
minidictionary2 = {'Fiction':[{'title': 'Gone With the Wind', 'author': 'Margaret Atwood', 'rating': 4.3, 'publisher': 'Macmillan Publishers', 'pages': 1037,
                               'language': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3,
                                'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}],
                   'Thrillers': [{'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK',
                                  'pages': 208, 'language': 'English'}],
                   'Humor': [{'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0,
                              'publisher': 'Hachette UK', 'pages': 336, 'language': 'English'}]}
minidictionary3 = {'Thrillers':[{'title': 'The Girl on the Train', 'author': 'Paula Hawkins', 'rating': 4.0, 'publisher': 'Turtleback Books', 'pages': 311,
                                 'language': 'English'}],
                   'Mystery': [{'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624,
                                'language': 'English'}],
                   'Classics': [{'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster',
                                 'pages': 320, 'language': 'English'}],
                   'Mythical Creatures':[{'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6,
                                          'publisher': 'Hachette UK', 'pages': 400, 'language': 'English'}]}
mini_dict1 = {'LGBTQ+': [{'title': "Title of Book", 'author': 'Favorite Author', 'rating': 3.6, 'publisher': 'Publishing Co', 'pages': 323, 'language': 'English'}, 
                         {'title': "Btitle", 'author': 'Book Writer', 'rating': 4.1, 'publisher': 'Publishing Co', 'pages': 14, 'language': 'English'}, 
                         {'title': "A Title", 'author': 'Tim Fulerton', 'rating': 4.3, 'publisher': 'Public Publish', 'pages': 563, 'language': 'English'}, 
                         {'title': "Atitle", 'author': 'Penny Craft', 'rating': 3.6, 'publisher': 'Ralph', 'pages': 785, 'language': 'English'}], 
              'Art': [{'title': "Rain", 'author': 'Book Writer', 'rating': 4.0, 'publisher': 'Domino', 'pages': 453, 'language': 'English'}, 
                      {'title': "Title of Book", 'author': 'Favorite Author', 'rating': 3.6, 'publisher': 'Publishing Co', 'pages': 323, 'language': 'English'}, 
                      {'title': "Genny", 'author': 'Favorite Author', 'rating': 5.0, 'publisher': 'Georgia Pub Inc', 'pages': 53, 'language': 'English'}], 
              'Cooking': [{'title': "Realness", 'author': 'Kenny', 'rating': 4.7, 'publisher': 'Ralph', 'pages': 203, 'language': 'English'}, 
                          {'title': "Chloe", 'author': 'Pluto', 'rating': 3.9, 'publisher': 'Apub', 'pages': 343, 'language': 'English'}]}
mini_dict2 = {'Fiction': [{'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3,
                           'publisher': 'Hachette UK', 'pages': 672, 'language': 'English'},
                          {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English'},
                          {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240,
                           'language': 'English'},
                          {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English'}],
              'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment',
                          'pages': 96, 'language': 'English'},
                    
                         {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English'}]}

#Case 1 Funciton
def sort_books_title(book_dictionary: dict)-> list:
    """
    Stephanie Sarria 101216262
    The function returns a list with the book data stored as a dictionary book where the books are sorted alphabetically by title.
    >>> sort_books_title(book_category_dictionary('google_books_dataset.csv')
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}......{'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English'}]
    
    """ 
    titles = category_change(book_dictionary)

    for i in range(len(titles)):
        for j in range(0 , (len(titles)) - i - 1):
            """
            if titles[j]['title'][0] == "'":
                if titles[j]['title'][1:-1] > titles[j+1]['title']:
                    titles[j], titles[j+1] = titles[j+1], titles[j]     
                    """
            if titles[j]['title'] > titles[j+1]['title']:
                titles[j], titles[j+1] = titles[j+1], titles[j]
    return titles

#Case 2 Function
def sort_books_publisher(dictfromcase1: dict) -> list:
    """
    Aditi Manjunath Keertani 101202033
    The function returns a list with the book data stored as a dictionary book where the books are
    sorted alphabetically by publisher. Books with the same publisher are sorted by title.
    >>>print(sort_books_publisher(dictionary_ex))
    [{'title': 'D', 'author': 'E', 'rating': 3.6, 'publisher': 'C', 'pages': 323, 'language': 'English', 'category': ['Cat1', 'Cat2']}, {'title': 'A', 'author': 'B', 'rating': 3.9, 'publisher': 'F', 'pages': 400, 'language': 'English', 'category': 'Cat1'}, {'title': 'I', 'author': 'J', 'rating': 5.0, 'publisher': 'H', 'pages': 200, 'language': 'English', 'category': 'Cat2'}, {'title': 'G', 'author': 'B', 'rating': 4.3, 'publisher': 'K', 'pages': 183, 'language': 'English', 'category': 'Cat2'}]
    """
    bookList = category_change(dictfromcase1)
    # sorting the list of dictionaries by publisher alphabetically
    for i in range(len(bookList)):
        for j in range(0, len(bookList) - 1 - i):
            if bookList[j]['publisher'] > bookList[j+1]['publisher']:
                bookList[j], bookList[j+1] = bookList[j+1], bookList[j]
    # sorting the list of dictionaries for  same publishers by title alphabetically

            if bookList[j]['publisher'] == bookList[j + 1]['publisher']:
                if bookList[j]['title'] > bookList[j + 1]['title']:
                    bookList[j], bookList[j + 1] = bookList[j + 1], bookList[j]
    return(bookList)

#Case 3 Function
def sort_books_author(input_dictionary: dict)->list:
    """
    Kit Horeczy 101189904
    Stephanie Sarria 101216262
    Aditi Manjunath Keertani 101202033
    Returns a list of books sorted by author when given a dictionary. Creates a 
    list of book dictionaries with category key altered to include all 
    categories the book can be found in. Sorts them alphabetically by author. 
    Books with the same rating are further sorted alphabetically by title.
    >>>print(sort_books_author(dictionary_ex))
    [{'title': 'A', 'author': 'B', 'rating': 3.9, 'publisher': 'F', 'pages': 400, 'language': 'English', 'category': 'Cat1'}, {'title': 'G', 'author': 'B', 'rating': 4.3, 'publisher': 'K', 'pages': 183, 'language': 'English', 'category': 'Cat2'}, {'title': 'D', 'author': 'E', 'rating': 3.6, 'publisher': 'H', 'pages': 323, 'language': 'English', 'category': 'Cat1'}, {'title': 'I', 'author': 'J', 'rating': 5.0, 'publisher': 'C', 'pages': 200, 'language': 'English', 'category': 'Cat2'}]
    """
    changed_list = category_change(input_dictionary)
    length = len(changed_list)
    for i in range(length):
        for j in range(0, length-i-1):
            # if authors are the same, sorts by tite
            if changed_list[j].get('author') == changed_list[j+1].get('author'):
                if changed_list[j].get('title') > changed_list[j+1].get('title'):
                    changed_list[j],changed_list[j+1] = changed_list[j+1], changed_list[j]
            #if authors are different, sorts by author
            if changed_list[j].get('author') != changed_list[j+1].get('author'):
                if changed_list[j].get('author') > changed_list[j+1].get('author'):
                    changed_list[j],changed_list[j+1] = changed_list[j+1], changed_list[j]
    return changed_list

#Case 4 Function
def sort_books_ascending_rate(input_dictionary:dict)->list:
    """
    Kit Horeczy 101189904
    Returns a list of books sorted by rating when given a dictionary. Creates a 
    list of book dictionaries with category key altered to include all 
    categories the book can be found in. Then sorts them by rate with N/A being
    lowest and first and 5 being highest and last. Books with the same rating
    are further sorted alphabetically by title
    >>>print(sort_books_ascending_rate(sample_dictionary))
    [{'title': 'Pal', 'author': 'Ren', 'rating': 'N/A', 'publisher': 'Herbert', 'pages': 100, 'language': 'English', 'category': 'CategoryA'}, {'title': 'Drew', 'author': 'Veronica', 'rating': 3.6, 'publisher': 'Hamlitlon', 'pages': 323, 'language': 'English', 'category': ['CategoryA', 'CategoryB']}, {'title': 'Rain', 'author': 'Paul', 'rating': 3.6, 'publisher': 'H', 'pages': 323, 'language': 'English', 'category': 'CategoryB'}]
    """
    changed_list = category_change(input_dictionary)
    length = len(changed_list)
    for i in range(length):
        for j in range(0, length-i-1):
            #if both ratings are N/A, sorts by title
            if (type(changed_list[j].get('rating')) == str) and (type(changed_list[j+1].get('rating')) == str):
                if changed_list[j].get('title') > changed_list[j+1].get('title'):
                    changed_list[j],changed_list[j+1] = changed_list[j+1], changed_list[j]
            #if comparing N/A and a number, sort N/A first
            if (type(changed_list[j].get('rating')) == str) and (type(changed_list[j+1].get('rating')) == float):
                changed_list[j],changed_list[j+1] = changed_list[j],changed_list[j+1]
            if (type(changed_list[j].get('rating')) == float) and (type(changed_list[j+1].get('rating')) == str):
                changed_list[j],changed_list[j+1] = changed_list[j+1],changed_list[j]
            #if both ratings are floats, sorts by rating number
            if (type(changed_list[j].get('rating')) == float) and (type(changed_list[j+1].get('rating')) == float):
                if changed_list[j].get('rating') > changed_list[j+1].get('rating'):
                    changed_list[j],changed_list[j+1] = changed_list[j+1], changed_list[j]
                #if both ratings are the same, sorts by title
                if changed_list[j].get('rating') == changed_list[j+1].get('rating'):
                    if changed_list[j].get('title') > changed_list[j+1].get('title'):
                        changed_list[j],changed_list[j+1] = changed_list[j+1], changed_list[j]
    return changed_list

# Main script - tests
if __name__ == "__main__":
    # Case 1
    def sort_books_title_test():
        """
        Kit Horeczy 101189904
        returns True and prints "sort_books_title: Passed" if code passes unit
        testing. if it fails, returns False and prints "sort_books_title: FAILED"
        >>>sort_books_title_test()
        sort_books_title: Passed
        True
        """
        if (check_equal("sort_books_title test 1:", sort_books_title(book_category_dictionary("test_008.csv")), [{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'language': 'English', 'category': 'Adventure'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'language': 'English', 'category': 'Adventure'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English', 'category': 'Adventure'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'language': 'English', 'category': 'Biography'}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352, 'language': 'English', 'category': 'Biography'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': 'Business'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English', 'category': 'Adventure'}, {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'rating': 5.0, 'publisher': 'Penguin', 'pages': 112, 'language': 'English', 'category': 'Biography'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': 4.6, 'publisher': 'Metropolitan Books', 'pages': 352, 'language': 'English', 'category': 'Biography'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English', 'category': 'Adventure'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'language': 'English', 'category': 'Biography'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English', 'category': 'Adventure'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'language': 'English', 'category': 'Adventure'}])) and (check_equal("sort_books_title test 2:", sort_books_title(mini_dict1),[{'title': 'A Title', 'author': 'Tim Fulerton', 'rating': 4.3, 'publisher': 'Public Publish', 'pages': 563, 'language': 'English', 'category': 'LGBTQ+'}, {'title': 'Atitle', 'author': 'Penny Craft', 'rating': 3.6, 'publisher': 'Ralph', 'pages': 785, 'language': 'English', 'category': 'LGBTQ+'}, {'title': 'Btitle', 'author': 'Book Writer', 'rating': 4.1, 'publisher': 'Publishing Co', 'pages': 14, 'language': 'English', 'category': 'LGBTQ+'}, {'title': 'Chloe', 'author': 'Pluto', 'rating': 3.9, 'publisher': 'Apub', 'pages': 343, 'language': 'English', 'category': 'Cooking'}, {'title': 'Genny', 'author': 'Favorite Author', 'rating': 5.0, 'publisher': 'Georgia Pub Inc', 'pages': 53, 'language': 'English', 'category': 'Art'}, {'title': 'Rain', 'author': 'Book Writer', 'rating': 4.0, 'publisher': 'Domino', 'pages': 453, 'language': 'English', 'category': 'Art'}, {'title': 'Realness', 'author': 'Kenny', 'rating': 4.7, 'publisher': 'Ralph', 'pages': 203, 'language': 'English', 'category': 'Cooking'}, {'title': 'Title of Book', 'author': 'Favorite Author', 'rating': 3.6, 'publisher': 'Publishing Co', 'pages': 323, 'language': 'English', 'category': ['LGBTQ+', 'Art']}])) and (check_equal("sort_books_title test 3:", sort_books_title(mini_dict2),[{'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English', 'category': 'Fiction'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English', 'category': 'Fiction'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English', 'category': 'Fiction'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English', 'category': 'Comics'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'language': 'English', 'category': 'Fiction'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English', 'category': 'Comics'}])) == True:
            print("sort_books_title: PASSED")
            return True
        else:
            print("sort_books_title: FAILED")
            return False

    # Case 2
    def sort_books_publisher_test():
        """
        Stephanie Sarria 101216262
        returns True and prints "sort_books_publisher: Passed" if code passes unit
        testing. if it fails, returns False and prints "sort_books_title: FAILED"
        >>>sort_books_publisher_test()
        sort_books_title: Passed
        """
        if (check_equal("sort_books_publisher test 1:", sort_books_publisher(mini_dict1),[{'title': 'Chloe', 'author': 'Pluto', 'rating': 3.9, 'publisher': 'Apub', 'pages': 343, 'language': 'English', 'category': 'Cooking'}, {'title': 'Rain', 'author': 'Book Writer', 'rating': 4.0, 'publisher': 'Domino', 'pages': 453, 'language': 'English', 'category': 'Art'}, {'title': 'Genny', 'author': 'Favorite Author', 'rating': 5.0, 'publisher': 'Georgia Pub Inc', 'pages': 53, 'language': 'English', 'category': 'Art'}, {'title': 'A Title', 'author': 'Tim Fulerton', 'rating': 4.3, 'publisher': 'Public Publish', 'pages': 563, 'language': 'English', 'category': 'LGBTQ+'}, {'title': 'Btitle', 'author': 'Book Writer', 'rating': 4.1, 'publisher': 'Publishing Co', 'pages': 14, 'language': 'English', 'category': 'LGBTQ+'}, {'title': 'Title of Book', 'author': 'Favorite Author', 'rating': 3.6, 'publisher': 'Publishing Co', 'pages': 323, 'language': 'English', 'category': ['LGBTQ+', 'Art']}, {'title': 'Atitle', 'author': 'Penny Craft', 'rating': 3.6, 'publisher': 'Ralph', 'pages': 785, 'language': 'English', 'category': 'LGBTQ+'}, {'title': 'Realness', 'author': 'Kenny', 'rating': 4.7, 'publisher': 'Ralph', 'pages': 203, 'language': 'English', 'category': 'Cooking'}])) and (check_equal("sort_books_publisher test 2:", sort_books_publisher(mini_dict2),[{'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English', 'category': 'Comics'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English', 'category': 'Fiction'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'language': 'English', 'category': 'Fiction'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English', 'category': 'Fiction'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English', 'category': 'Fiction'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English', 'category': 'Comics'}])) and (check_equal("sort_books_publisher test 3:", sort_books_publisher(book_category_dictionary("test_008.csv")),[{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': 'Business'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'language': 'English', 'category': 'Biography'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English', 'category': 'Adventure'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'language': 'English', 'category': 'Biography'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English', 'category': 'Adventure'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'language': 'English', 'category': 'Adventure'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'language': 'English', 'category': 'Adventure'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'language': 'English', 'category': 'Adventure'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English', 'category': 'Adventure'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': 4.6, 'publisher': 'Metropolitan Books', 'pages': 352, 'language': 'English', 'category': 'Biography'}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352, 'language': 'English', 'category': 'Biography'}, {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'rating': 5.0, 'publisher': 'Penguin', 'pages': 112, 'language': 'English', 'category': 'Biography'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English', 'category': 'Adventure'}])) == True:
            print("sort_books_author: PASSED")
            return True
        else:
            print("sort_books_author: FAILED")
            return False            

    # Case 3
    def sort_books_author_test():
        """
        Kit Horeczy 101189904
        Stephanie Sarria 101216262
        Aditi Manjunath Keertani 101202033
        returns True and prints "sort_books_author: Passed" if code passes unit
        testing. if it fails, returns False and prints "sort_books_author: FAILED"
        >>>sort_books_author_test()
        sort_books_author: Passed
        True
        """    
        if (check_equal("sort_books_author test 1:", sort_books_author(book_category_dictionary("test_008.csv")),[{'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English', 'category': 'Adventure'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English', 'category': 'Adventure'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English', 'category': 'Adventure'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'language': 'English', 'category': 'Biography'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English', 'category': 'Adventure'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'language': 'English', 'category': 'Biography'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'language': 'English', 'category': 'Adventure'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English', 'category': 'Business'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': 4.6, 'publisher': 'Metropolitan Books', 'pages': 352, 'language': 'English', 'category': 'Biography'}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352, 'language': 'English', 'category': 'Biography'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'language': 'English', 'category': 'Adventure'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'language': 'English', 'category': 'Adventure'}, {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'rating': 5.0, 'publisher': 'Penguin', 'pages': 112, 'language': 'English', 'category': 'Biography'}])) and (check_equal("sort_books_author test 2:", sort_books_author(mini_dict1), [{'title': 'Btitle', 'author': 'Book Writer', 'rating': 4.1, 'publisher': 'Publishing Co', 'pages': 14, 'language': 'English', 'category': 'LGBTQ+'}, {'title': 'Rain', 'author': 'Book Writer', 'rating': 4.0, 'publisher': 'Domino', 'pages': 453, 'language': 'English', 'category': 'Art'}, {'title': 'Genny', 'author': 'Favorite Author', 'rating': 5.0, 'publisher': 'Georgia Pub Inc', 'pages': 53, 'language': 'English', 'category': 'Art'}, {'title': 'Title of Book', 'author': 'Favorite Author', 'rating': 3.6, 'publisher': 'Publishing Co', 'pages': 323, 'language': 'English', 'category': ['LGBTQ+', 'Art']}, {'title': 'Realness', 'author': 'Kenny', 'rating': 4.7, 'publisher': 'Ralph', 'pages': 203, 'language': 'English', 'category': 'Cooking'}, {'title': 'Atitle', 'author': 'Penny Craft', 'rating': 3.6, 'publisher': 'Ralph', 'pages': 785, 'language': 'English', 'category': 'LGBTQ+'}, {'title': 'Chloe', 'author': 'Pluto', 'rating': 3.9, 'publisher': 'Apub', 'pages': 343, 'language': 'English', 'category': 'Cooking'}, {'title': 'A Title', 'author': 'Tim Fulerton', 'rating': 4.3, 'publisher': 'Public Publish', 'pages': 563, 'language': 'English', 'category': 'LGBTQ+'}])) and (check_equal("sort_books_author test 3:", sort_books_author(mini_dict2),[{'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English', 'category': 'Comics'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English', 'category': 'Fiction'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English', 'category': 'Fiction'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English', 'category': 'Comics'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'language': 'English', 'category': 'Fiction'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English', 'category': 'Fiction'}])) == True:
            print("sort_books_author: PASSED")
            return True
        else:
            print("sort_books_author: FAILED")
            return False

    # Case 4
    def sort_books_ascending_rate_test():
        """
        Aditi Manjunath Keertani 101202033
        returns True and prints "sort_books_acsending_rate: Passed" if code passes unit
        testing. if it fails, returns False and prints "sort_books_title: FAILED"
        >>>sort_books_ascending_rate_test()
        sort_books_title: Passed
        """
        if (check_equal("sort_books_ascending_rate test 1:", sort_books_ascending_rate(minidictionary1), [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'language': 'English', 'category': 'Legal'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English', 'category': 'Horror'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'language': 'English', 'category': 'Information Technology'}, {'title': 'Rich Dad Poor Dad', 'author': 'Robert Kiyosaki', 'rating': 4.7, 'publisher': 'Warner Books', 'pages': 366, 'category': 'Investing', 'language': 'English'}])) and (check_equal("sort_books_ascending_rate test 2:", sort_books_ascending_rate(minidictionary2), [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English', 'category': 'Fiction'}, {'title': 'Gone With the Wind', 'author': 'Margaret Atwood', 'rating': 4.3, 'publisher': 'Macmillan Publishers', 'pages': 1037, 'category': 'Fiction', 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English', 'category': 'Thrillers'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'language': 'English', 'category': 'Humor'}])) and (check_equal("sort_books_ascending_rate test 3:", sort_books_ascending_rate(minidictionary3), [{'title': 'The Girl on the Train', 'author': 'Paula Hawkins', 'rating': 4.0, 'publisher': 'Turtleback Books', 'pages': 311, 'language': 'English', 'category': 'Thrillers'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'language': 'English', 'category': 'Mystery'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'language': 'English', 'category': 'Classics'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English', 'category': 'Mythical Creatures'}])) == True:
            print("sort_books_author: PASSED")
            return True
        else:
            print("sort_books_author: FAILED")
            return False  
    # All together
    if sort_books_title_test() and sort_books_author_test() and sort_books_ascending_rate_test() and sort_books_publisher_test() == True:
        print("All tests PASSED")
