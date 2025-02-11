#Team 008
# Kit Horeczy 101189904 2, 3, 4
# Stephanie Sarria 101216262 5, 6, 7
# Aditi Manjunath Keertani 101202033 1, 8

from unit_testing import check_equal
from T008_P5_load_data import book_category_dictionary

#Function 1: Add book
def add_book(dictfromcase1: dict, tp1: tuple) -> dict:
    '''
    Aditi Manjunath Keertani
    The function adds the book to the dictionary and verifies that the book has
    been added. The function returns the updated dictionary and prints a message
    stating, “The book has been added correctly” or “There was an error
    adding the book”.
    >>>The book has been added correctly
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'language': 'English'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'language': 'English'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 416, 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'language': 'English'}, {'title': 'A Trace of Vice (a Keri Locke Mystery Book #3)', 'author': 'Blake Pierce', 'rating': 4.8, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'language': 'English'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208, 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'language': 'English'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216, 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'language': 'English'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250, 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250, 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'language': 'English'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'language': 'English'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60, 'language': 'English'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728, 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English'}], 'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English'}, {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'pages': 144, 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 128, 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'language': 'English'}, {'title': 'The Joker', 'author': 'Brian Azzarello', 'rating': 4.4, 'publisher': 'DC', 'pages': 130, 'language': 'English'}, {'title': 'Venomized', 'author': 'Cullen Bunn', 'rating': 4.5, 'publisher': 'Marvel Entertainment', 'pages': 136, 'language': 'English'}], 'Economics': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'language': 'English'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English'}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2', 'author': 'Brian Tracy', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'pages': 288, 'language': 'English'}, {'title': 'The Power of Habit: Why We Do What We Do in Life and Business', 'author': 'Charles Duhigg', 'rating': 4.1, 'publisher': 'Random House', 'pages': 416, 'language': 'English'}, {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English'}, {'title': 'Getting Things Done: The Art of Stress-Free Productivity', 'author': 'David Allen', 'rating': 4.5, 'publisher': 'Penguin', 'pages': 352, 'language': 'English'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'pages': 176, 'language': 'English'}, {'title': 'Rework', 'author': 'Jason Fried', 'rating': 4.1, 'publisher': 'Currency', 'pages': 288, 'language': 'English'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'language': 'English'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'language': 'English'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English'}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'rating': 4.7, 'publisher': 'Simon and Schuster', 'pages': 592, 'language': 'English'}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'rating': 4.6, 'publisher': 'Penguin', 'pages': 256, 'language': 'English'}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'rating': 3.8, 'publisher': 'Harper Collins', 'pages': 336, 'language': 'English'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'rating': 5.0, 'publisher': 'Simon and Schuster', 'pages': 224, 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'language': 'English'}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'rating': 4.7, 'publisher': 'Berrett-Koehler Publishers', 'pages': 144, 'language': 'English'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pages': 14, 'language': 'English'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 320, 'language': 'English'}, {'title': 'Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports', 'author': 'Thomas Ittelson', 'rating': 4.0, 'publisher': 'Red Wheel/Weiser', 'pages': 288, 'language': 'English'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'rating': 4.6, 'publisher': 'HarperCollins Leadership', 'pages': 288, 'language': 'English'}], 'Business': [{'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'language': 'English'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'pages': 176, 'language': 'English'}, {'title': 'Principles: Life and Work', 'author': 'Ray Dalio', 'rating': 4.7, 'publisher': 'Simon and Schuster', 'pages': 592, 'language': 'English'}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'rating': 4.5, 'publisher': 'W. W. Norton & Company', 'pages': 256, 'language': 'English'}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'rating': 3.8, 'publisher': 'Penguin', 'pages': 272, 'language': 'English'}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'rating': 4.5, 'publisher': 'W. W. Norton & Company', 'pages': 256, 'language': 'English'}, {'title': 'Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3', 'author': 'Brian Tracy', 'rating': 4.7, 'publisher': 'Berrett-Koehler Publishers', 'pages': 144, 'language': 'English'}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'rating': 4.5, 'publisher': 'W. W. Norton & Company', 'pages': 256, 'language': 'English'}, {'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English'}, {'title': 'Selling 101: What Every Successful Sales Professional Needs to Know', 'author': 'Zig Ziglar', 'rating': 3.8, 'publisher': 'HarperCollins Leadership', 'pages': 112, 'language': 'English'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'language': 'English'}, {'title': 'The Magic of Thinking Big', 'author': 'David J. Schwartz', 'rating': 4.6, 'publisher': 'Penguin', 'pages': 256, 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'language': 'English'}, {'title': 'Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain', 'author': 'Steven D. Levitt', 'rating': 4.3, 'publisher': 'Harper Collins', 'pages': 304, 'language': 'English'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 'N/A', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pages': 14, 'language': 'English'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'rating': 5.0, 'publisher': 'Simon and Schuster', 'pages': 224, 'language': 'English'}, {'title': 'Rework', 'author': 'Jason Fried', 'rating': 4.1, 'publisher': 'Currency', 'pages': 288, 'language': 'English'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'rating': 4.6, 'publisher': 'HarperCollins Leadership', 'pages': 288, 'language': 'English'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 320, 'language': 'English'}], 'Detective': [{'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'language': 'English'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'language': 'English'}, {'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'pages': 208, 'language': 'English'}, {'title': 'Watching (The Making of Riley Paige Book 1)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}], 'Psychology': [{'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'pages': 320, 'language': 'English'}, {'title': 'Predictably Irrational: The Hidden Forces that Shape Our Decisions', 'author': 'Dan Ariely', 'rating': 4.0, 'publisher': 'HarperCollins UK', 'pages': 304, 'language': 'English'}], 'Fantasy': [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'language': 'English'}, {'title': 'Mistborn Trilogy: The Final Empire. The Well of Ascension. The Hero of Ages', 'author': 'Brandon Sanderson', 'rating': 4.7, 'publisher': 'Tor Books', 'pages': 1712, 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'language': 'English'}, {'title': 'The Lord of the Rings: The Fellowship of the Ring. The Two Towers. The Return of the King', 'author': 'J. R. R. Tolkien', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 1216, 'language': 'English'}, {'title': 'The Weight of Honor (Kings and Sorcerers Book 3)', 'author': 'Morgan Rice', 'rating': 4.4, 'publisher': 'Morgan Rice', 'pages': 250, 'language': 'English'}, {'title': 'Night of the Bold (Kings and Sorcerers Book 6)', 'author': 'Morgan Rice', 'rating': 4.3, 'publisher': 'Morgan Rice', 'pages': 250, 'language': 'English'}, {'title': 'The Vagrant (The Vagrant Trilogy)', 'author': 'Peter Newman', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'language': 'English'}, {'title': 'Prince of Thorns (The Broken Empire. Book 1)', 'author': 'Mark Lawrence', 'rating': 4.2, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades. The Providence of Fire. The Last Mortal Bond)", 'author': 'Brian Staveley', 'rating': 4.3, 'publisher': 'Macmillan', 'pages': 1728, 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'language': 'English'}], 'Humor': [{'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'language': 'English'}, {'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'pages': 112, 'language': 'English'}], 'Crime': [{'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'language': 'English'}], 'Thrillers': [{'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'language': 'English'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'language': 'English'}, {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'rating': 4.5, 'publisher': 'Hachette UK', 'pages': 944, 'language': 'English'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'language': 'English'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 416, 'language': 'English'}, {'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'language': 'English'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': 4.3, 'publisher': 'Minotaur Books', 'pages': 60, 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}], 'Mystery': [{'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'pages': 624, 'language': 'English'}, {'title': 'Watching (The Making of Riley Paige Book 1)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'language': 'English'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'language': 'English'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'language': 'English'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery Book 5)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'language': 'English'}, {'title': 'Once Missed (A Riley Paige Mystery Book 16)', 'author': 'Blake Pierce', 'rating': 4.4, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': 4.5, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'language': 'English'}, {'title': 'A Trace of Crime (a Keri Locke Mystery Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'pages': 250, 'language': 'English'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'pages': 416, 'language': 'English'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'language': 'English'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'language': 'English'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'rating': 4.0, 'publisher': 'Hachette UK', 'pages': 448, 'language': 'English'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English'}], 'Classics': [{'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'pages': 320, 'language': 'English'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English'}], 'Adventure': [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'language': 'English'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'language': 'English'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 96, 'language': 'English'}], 'Superheroes': [{'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'rating': 4.0, 'publisher': 'Marvel Entertainment', 'pages': 96, 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': 4.2, 'publisher': 'DC Comics', 'pages': 448, 'language': 'English'}, {'title': 'Spider-Verse: Volume 1', 'author': 'Dan Slott', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 624, 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': 4.1, 'publisher': 'DC', 'pages': 164, 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': 4.4, 'publisher': 'Marvel Entertainment', 'pages': 128, 'language': 'English'}], 'Biography': [{'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352, 'language': 'English'}, {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'rating': 5.0, 'publisher': 'Penguin', 'pages': 112, 'language': 'English'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'language': 'English'}, {'title': 'Boy Erased: A Memoir', 'author': 'Garrard Conley', 'rating': 4.0, 'publisher': 'Penguin', 'pages': 352, 'language': 'English'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': 4.6, 'publisher': 'Metropolitan Books', 'pages': 352, 'language': 'English'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'language': 'English'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': 4.6, 'publisher': 'Metropolitan Books', 'pages': 352, 'language': 'English'}], 'Social Science': [{'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'rating': 4.2, 'publisher': 'Vintage', 'pages': 32, 'language': 'English'}, {'title': 'Happy: Why More or Less Everything is Absolutely Fine', 'author': 'Derren Brown', 'rating': 4.0, 'publisher': 'Random House', 'pages': 576, 'language': 'English'}, {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'author': 'Steven D. Levitt', 'rating': 3.8, 'publisher': 'Harper Collins', 'pages': 336, 'language': 'English'}], 'Mythical Creatures': [{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English'}], 'Epic': [{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'language': 'English'}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': 400, 'language': 'English'}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 4544, 'language': 'English'}, {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'rating': 4.7, 'publisher': 'Hachette UK', 'pages': 688, 'language': 'English'}], 'Horror': [{'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English'}], 'Traditional': [{'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': 40, 'language': 'English'}], 'Finance': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'language': 'English'}], 'Legal': [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': 384, 'language': 'English'}], 'Management': [{'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': 112, 'language': 'English'}], 'Money Management': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'language': 'English'}], 'Information Technology': [{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'language': 'English'}], 'Investing': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'language': 'English'}, {'title': 'Intelligent Investor', 'author': 'Benjamin Graham', 'rating': 4.5, 'publisher': 'Harper and Brothers', 'pages': 640, 'category': 'Investing', 'language': 'English'}]}
    '''
    tp = ()
    title = str(tp1[0])
    author = str(tp1[1])
    rating = float(tp1[2])
    publisher = str(tp1[3])
    pages = int(tp1[4])
    category = str(tp1[5])
    language = str(tp1[6])
    tp1 = (title, author, rating, publisher, pages, category, language)
    temp_book = {}
    for key in dictfromcase1.copy():
        if key == category:
            temp_book={}
            temp_book.update({"title": str(tp1[0]), "author": str(tp1[1]), "rating": float(tp1[2]), "publisher": str(tp1[3]), "pages": int(tp1[4]), "category" : str(tp1[5]), "language": str(tp1[6])})           
            dictfromcase1[key].append(temp_book)
    if temp_book in dictfromcase1[category]:
        print("The book has been added correctly")
    else:
        print("There was an error adding the book")
    return dictfromcase1

#Funciton 2: Remove Book
def remove_book(book_dictionary:dict, book_title: str, category_of_book: str)->dict:
    """
    Kit Horeczy
    Removes existing book given its title and category
    returns altered dictionary
    >>>remove_book(book_category_dictionary("google_books_dataset.csv"),"Boy Erased: A Memoir", Biography")
    The book has been removed correctly
    >>>remove_book(book_category_dictionary("google_books_dataset.csv"),"How To Win Friends and Influence People","Mystery")
    There was an error removing the book. Book not found.
    #wrong category
    >>>remove_book(book_category_dictionary("google_books_dataset.csv"),"Loveless", "Fiction")
    There was an error removing the book. Book not found.
    #non existant book
    """
    altered_book_dictionary = {}
    altered_book_dictionary.update(book_dictionary)
    category_dictionary = altered_book_dictionary.get(category_of_book)         #creates a list of every book dictionary in the desired category
    list_of_books = []
    random_list = []
    if category_of_book in book_dictionary:
        for book_info in category_dictionary:                                       #for every book in desired category
            list_of_books.append(book_info.get('title'))                            #add title to list_of_books
        if book_title in list_of_books:                                             #if the desired title is in the list of books in that category
            for title_dict in category_dictionary:                                  #for every book dictionary in desired category
                if title_dict.get('title') != book_title:                           #if the book dictionary is for a book with a name that isnt the desired book
                    random_list.append(title_dict)
                    altered_book_dictionary.update({category_of_book:(random_list)})
        elif book_title not in list_of_books:
            print("There was an error removing the book. Book not found.")
        if altered_book_dictionary != book_dictionary:
            print("The book has been removed correctly")
    return altered_book_dictionary 

#Function 3: Get Books by Category
def get_books_by_category(book_dictionary:dict, category_wanted:str)->int:
    """
    Kit Horeczy
    Returns number of books in category given dictionary it uses and the
    category wanted (with the first letter capitalized)
    prints title and author of each book in
    category
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Traditional")
    The category Traditional has 1 books. This is the list of books:
    Book 1 : The Red Signal: An Agatha Christie Short Story by Agatha Christie
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Fiction")
    The category Crime has 4 books. This is the list of books:
    Book 1 : Bring Me Back by B A Paris
    Book 2 : Total Control by David Baldacci
    Book 3 : Final Option: 'The best one yet' by Clive Cussler
    Book 4 : The Black Box by Michael Connelly
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Humor")
    The category Humor has 2 books. This is the list of books:
    Book 1 : Tall Tales and Wee Stories: The Best of Billy Connolly by Billy Connolly
    Book 2 : Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt by Adam Kay
    """
    category_dictionary = book_dictionary.get(category_wanted)
    num_of_books_category = 0
    book_num = 0
    book_info = []
    if category_wanted in book_dictionary:
        for books in category_dictionary:                                           #for every book of that category
            book_num += 1
        print("The category", category_wanted, "has", book_num,
              "books. This is the list of books:")                                  #prints list intro and num of books
        book_num2 = 0
        for books in category_dictionary:
            book_num2 += 1
            print("Book",book_num2,":",books.get('title'),"by",books.get('author')) #prints book "list"
    return book_num                                                             #returns number of books in category

#Function 4: Get Books by Rate
def get_books_by_rate(book_dictionary:dict, rating_wanted:int) ->int:
    """
    Kit Horeczy
    Returns number of books with a rating equal to, or within one integer of the
    desired rating, desired rating must be a positive integer
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"),3)
    There are 8 books whose rate is between 3 and 4 This is the list of books:
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2 : Bring Me Back by B A Paris
    Book 3 : Mrs. Pollifax Unveiled by Dorothy Gilman
    Book 4 : How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 5 : The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 6 : Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 7 : The Infinite Game by Simon Sinek
    Book 8 : Selling 101: What Every Successful Sales Professional Needs to Know by Zig Ziglar
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"),5)
    There are 5 books whose rate is between 5 and 6 This is the list of books:
    Book 1 : Final Option: 'The best one yet' by Clive Cussler
    Book 2 : The Red Signal: An Agatha Christie Short Story by Agatha Christie
    Book 3 : Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk by Michael Sincere
    Book 4 : Tall Tales and Wee Stories: The Best of Billy Connolly by Billy Connolly
    Book 5 : No One Is Too Small to Make a Difference by Greta Thunberg    
    """
    num_of_books_rate = 0
    list_of_books = []
    random_list = []
    book_num2 = 0
    max_rating = rating_wanted + 1
    for dictionaries in book_dictionary.items():
        for book in dictionaries[1]:
            if book.get('rating') != "N/A":
                if rating_wanted <= book.get('rating') < max_rating:
                    if book.get('title') not in random_list:
                        list_of_books.append([book.get('title'),book.get('author')])
                        random_list.append(book.get('title'))
    book_num = len(list_of_books)
    print("There are", book_num,
          "books whose rate is between", rating_wanted,
          "and", max_rating,
          "This is the list of books:")
    for i in list_of_books:
        book_num2 += 1
        print("Book", book_num2, ":", list_of_books[book_num2-1][0], "by", list_of_books[book_num2-1][1])
    return book_num2

#Function 5: Get Books by Title
def get_books_by_title(book_dictionary: dict, title_name: str)-> bool:
    """
    Stephanie Sarria
    if book exists, prints "This book has been found" and returns True, if book
    does not exist, prints "This book has not been found" and returns False
    """
    for category in book_dictionary.items():
        #print(category)
        for book in category[1]:
            #print(book)
            if title_name in book["title"]:
                #title_add = print(input(title_name), " is already in book list")
                print("This book has been found")
                return True
    print("This book has not been found")
    #print(title_name, " is not in list")
    return False

#Function 6: Get Books by Author
def get_books_by_author(book_dictionary: dict , author_name: str):
    """
    Stephanie Sarria
    returns number of books by author and prints a list of the books
    """
    book_num2 = 0
    lst = []
    lst2 = []
    for dictionaries in book_dictionary.items():
        #print(dictionaries)
        for book in dictionaries[1]:
            #print("haha",book)
            if book.get('author') == author_name:
            #if author_name in book["author"]:
                if book.get('title') not in lst2:
                    lst.append([book.get('title'),book.get('rating')])
                    lst2.append(book.get('title'))
    book_num = len(lst)
    print("The author", author_name, "has published the following books:")
    for i in lst:
        print("Book", book_num2+1,":", lst[book_num2][0], "rate:", lst[book_num2][1])
        book_num2 += 1
    return book_num

#Function 7: Get Books by Publisher
def get_books_by_publisher(book_dictionary: dict , publisher: str):
    """
    Stephanie Sarria
    returns number of books with given publisher and prints a list of those books
    """
    book_num2 = 0
    lst = []
    lst2 = []
    for dictionaries in book_dictionary.items():
        for book in dictionaries[1]:
            if book.get('publisher') == publisher:
                if book.get('title') not in lst2:
                    lst.append([book.get('title'),book.get('author')])
                    lst2.append(book.get('title'))
    book_num = len(lst)
    print("The publisher", publisher, "has published the following books:")
    for i in lst:
        print("Book", book_num2+1,":", lst[book_num2][0], "author:", lst[book_num2][1])
        book_num2 += 1
    return book_num

#Function 8: Get All Categories for Book Title
def get_all_categories_for_book_title(dictfromcase1: dict, title: str) -> int:
    '''
    Aditi Manjunath Keertani
    The function returns the number of categories associated with the given title.
    Additionally, the function prints the titles along with the category it belongs to.
    >>>The Book Title Antiques Roadkill: A Trash 'n' Treasures Mystery belongs to the following categories: 
    Category 1 :  Detective
    Category 2 :  Mystery
    Category 3 :  Fiction
    3
    >>>The Book Title The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further belongs to the following categories: 
    Category 1 :  Business
    Category 2 :  Finance
    Category 3 :  Economics
    Category 4 :  Investing
    Category 5 :  Money Management
    5
    >>>The Book Title Sword of Destiny: Witcher 2: Tales of the Witcher belongs to the following categories: 
    Category 1 :  Adventure
    Category 2 :  Mythical Creatures
    Category 3 :  Fiction
    3
    '''
    print("The Book Title", title, "belongs to the following categories: ")
    temp_set = set()
    count = 0
    
    for key in dictfromcase1:
        for values in dictfromcase1[key]:
            for item in values:
                if values[item] == title:
                    category = key
                    count +=1
                    temp_set.add(category)
    
    count = 0               
    for x in temp_set:
        count +=1
        print("Category", count,': ', x)
        
    return count

#Function 1 (add_book)
def test_function_one():
    """
    returns True if function successful and False if function fails
    """
    small_dict = {'Fiction': [{'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'language': 'English'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'language': 'English'}], 'Detective': [{'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'language': 'English'}], 'Crime': [{'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'pages': 368, 'language': 'English'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'language': 'English'}], 'Investing': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'language': 'English'}], 'Mystery': [{'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'language': 'English'}], 'Thrillers': [{'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': 5.0, 'publisher': 'Penguin UK', 'pages': 400, 'language': 'English'}]}
