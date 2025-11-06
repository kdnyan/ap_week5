# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.
magic = "abracadabra"
fifth_char = print(magic[4])
second_to_last_char = print(magic[-2])
first_c_index = print(magic.index('c'))
first_c_index = print(magic.index('r'))
last_a_index = print(magic.rindex('a'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

hij = print(alphabet.index('hij'))
hij2 = print (alphabet[7:10])


# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
every_second = print(alphabet[0:13:2])
m_index = print(alphabet.index('m'))
# c. Reverse the entire string using slicing.
reverse_alphabet = print(alphabet[: :-1])
# Problem Set 2: Extracting Information


i_have_a_dream = "And so let freedom ring. From the prodigious hilltops of New Hampshire, let freedom ring! From the mighty mountains of New York, let freedom ring! From the Alleghenies of Pennsylvania, let freedom ring! From the snow-capped Rockies of Colorado, let freedom ring! From the curvaceous slopes of California, let freedom ring! But not only that: Let freedom ring from Stone Mountain of Georgia. Let freedom ring from Lookout Mountain of Tennessee. Let freedom ring from every hill and molehill of Mississippi, from every mountainside, let freedom ring."
reverse_i_have_a_dream = print (i_have_a_dream[: :-1])

# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

famous_quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

dash_index = famous_quote.find('-')
extracted_name = famous_quote[dash_index + 2:]  # +2 to skip "- "

print(extracted_name)
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
info = "Python is fun. Fun is good. Good is subjective." 
third_letter = print(info[::3])
m_index = print(info.index('subjective'))
extracted_word = print (info[36:])
words = info.split()
print(words)
reversed_words = ' '. join(reversed(words))
print(reversed_words)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
text = "MAY THE FORCE BE WITH YOU"
lowercase_string = text.lower()
print(lowercase_string)
motto = ("Make","hastle","slowly.")
joined_motto= '/'.join(motto)
print(joined_motto)
joined_motto_split= joined_motto.split('a')
print (joined_motto_split)
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
sentence = "Life is what happens when you are busy making other plans."
replaced_sentence = sentence.replace("busy", "distracted").replace("plans", "mistakes")
print(replaced_sentence) 
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repeated_word = "Iteration " * 7
print(repeated_word)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word = "moonlight"
quote = "With freedom, books, flowers, and the moon, who could could be happy? - Oscar Wilde"

word_in_quote = word in quote
print(word_in_quote)

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.