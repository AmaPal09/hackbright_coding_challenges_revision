# By default, when you print text to the terminal, the text automatically takes 
# up the entire width of the terminal. If the line is too long, terminals will 
# wrap the text and continue it on another line. However, most terminals don’t 
# wrap text intelligently — sometimes they’ll break words like this:

Hello, this is a really long line. The char
cter limit is 43 though, so the word 'chara
cter' is butchered.
# It would be nice if instead, text was wrapped without breaking words:

Hello, this is a really long line. The
character limit is 43 though, so the word
'character' is butchered.
# Write a function that takes in a string and a character limit (as an integer). 
# It should print the contents of the string without going over the character 
# limit and without breaking words. For example:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
Hello,
world! I
love
Python and
Hackbright

# Your test input will never contain a character limit that is smaller than the 
# largest continuous sequence of non-whitespace characters (however, this is a 
#     great edge case to handle as an additional challenge!)
# We’ve provided fit-to-width.py which contains test cases and a function stub 
# for you to complete.