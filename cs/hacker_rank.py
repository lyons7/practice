# Jewels and Stones problem
# You're given strings J representing the types of stones that are jewels, and S representing the stones you have. Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels. The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example input:
J = "aA"
S = "aAAbbbb"

# Output would be 3
J = "z"
S = "ZZ"
# Output: 0

# Solution
def numJewelsInStones(J, S): # Define function
    return sum(S.count(j) for j in J) # This is saying give me the sum of how many times j shows up in S for all of the js in J

numJewelsInStones(J,S)

# Morse Code problem: International Morse Code has a standard mapping of dots and dashes to letters. We want to feed in groups of letters and get
# the morse code equivalent back!

# Morse code mapping:
morse_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

# Example input:
words = ["gin", "zen", "gig", "msg"]
def uniqueMorserepresentations(words):
    morse_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    let = 'abcdefghijklmnopqrstuvwxyz'
    mapping = {i[0]: i[1] for i in zip(let, morse_alphabet)} # Zip is mapping similar index of mutliple containers so they can be used as a single entity
    mozs = set() # Set just keeps unique elements
    for w in words:
            string = ''.join([mapping[c] for c in w]) # Mapping is matching those two things up
            mozs.add(string)

    return (len(mozs))

uniqueMorserepresentations(words)

# Get Morse translation for a word
word = 'shark'
def morsecode(word):
    morse_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = {i[0]:i[1] for i in zip(alphabet, morse_alphabet)}
    s = ''
    for w in word:
        string = ''.join([mapping[c] for c in w])
        s += string
    return s

morsecode(word)


# Check whether or not a year is a leap year or not
# If year is divisible by 4, leap year UNLESS it's divisible by 100 UNLESS it's divisible by 400...
# Start with absolute base case we know is always correct
def is_leap(year):
    leap = False
    if year % 400 == 0: # Percent sign is saying remainder -- this is how we check is something is evenly divisable. Here we say if year evenly by 400 --> leap for sure
        leap = True
    elif year % 100 != 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = 2018
is_leap(year)


# Check if unique all strings
x = 'Insight is going well'
def findifunique(x):
  z = []
  for i in x:
    if i not in z:
      z.append(i)
    else:
      continue
  if len(x) == len(z):
    print('Yes unique!')
  else:
    print('Not unique!') #aka "narp"
findifunique('fnldasndlkamsdamdadmas')
findifunique(x)

# Enumerate enables you to use extra features
# Compare this:
string1 = "cat"

for char in string1:
    print(char)

# To this:
string1 = "cat"

for index, char in enumerate(string1):
    print(char,"at index ",index)

# what does 'enumerate' do?
# look at the variables that you get in the for loop. First, you get i, which is the item value in x at that specific position, you also get index, which is the indexed position
# it basically adds a counter to the variable, sort of like range(len(x))
# so its shorthand? for range(len(x))
# AF
# we're using ALL THE CHATS
# aka tous les chats ^o.o^~

# New problem!
# What we want to do is swap the first letter with the last letter
word='caturday'
# Function
def front_back(str):
  #front should give first char
  front=str[0:1]
  #back should give last char
  back=str[-1:]
  #middle should be the middle part with 1st and last char removed
  middle= str[1:-1]
  return back+middle+front

front_back(word)

# This does a similar thing
# this works similarly, but i have no clue why
a = 'python is odd'
a[::-1]
# Somehow flips a string!


# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and
# backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# 'able was I, ere I saw Elba'
# 'mad am I madam'
# Does not have to be a word in the dictionary, can be any set of characters that has a "palindromic fashion". (-Kate Lyons)
# A.K.A.: Can you make a palindrome out of this thing?

#str.count() Returns the number of times a
#specified value occurs in a string
def permupali(maybe):
  odd = 0 # Start odd out at 0
  for i in maybe: # For each letter in our string
    if maybe.count(i)%2 != 0: # If the remainder of number of letters in that string
      odd += 1 # is not 0 i.e. (if it isn't even) -- add 1 to the odd counter
  if odd <= 1: # If our odd counter is less than or equal to 1, yes we have a permutation
    return True
  else:
    return False

# Try it out
s1 = "malay   mala"
s2 = "ab  c  ba"
s3 = 'aabb'
permupali(s3)

# Two strings
# Given two strings, determine if they share a common substring. A substring may be as small as one character.
# For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
# What we want to do is say, go thru these strings and check if there is a match for any of these letters. If there is -- TRUE if not FALSE!
# Basically, this is a search!
s1 = 'cat'
s2 = 'taco'

def twoStrings(s1,s2):
    set1 = set(s1)
    set2 = set(s2)
    if set1.intersection(set2): # intersection gives largest set which contains all elements that are common to both sets
        return True
    else:
        return False

twoStrings(s1,s2)

# Roman numeral problem. We want to provide an integer and get a roman numeral back. There are special rules for 5s and 9s
# however.
# The rules are:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
def intToRoman(num):
    result = ''
    d = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),  (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    # Making a list of pairs (tuple) as a sort of dictionary to keep track of things)
    for one_tuple in d: # For an entry in our list of pairs
        while num >= one_tuple[0]: # while the number is more than or equal to the first part of tuple pair (1,000)
            result += one_tuple[1] # Result whatever is there at the second part of the tuple
            num -= one_tuple[0] # Then adjust our number at the 0 position
            # This will continue until the number is less than any of the first pairs in our tuple (down to 0!)
    return result
num = 28
intToRoman(num)
650%10

# Encode and decode TinyURL
# You want to make two functions, one that creates a tinyURL and another one that 'translates' it to the original URL
# This involves a hash table?
class Codec:
    def __init__(self):
        self.dct = {} # Start with an empty dictionary
        self.key = 0 # We start at 0?

    def encode(self, longUrl):
        dct = {} # Start with an empty dictionary
        key = 0 # We start at 0?
        # Encodes a URL to a shortened URL.
        self.key += 1 # For each pass, increase key by 1
        txt = "tinurl" + str(self.key) #You'll now create the tiny URL with that key
        self.dct[txt] = longUrl # Create a dictionary entry in which you've connected the text in your dictionary to the long URL
        return txt # Give back the text which is the longUrl

    def decode(self, shortUrl):
        # Decodes a shortened URL to its original URL.
        return self.dct[shortUrl] # This is saying give me whatever is at the shortURL position in the dictionary

url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
codec.decode(codec.encode(url))
codec.encode(url)
shortUrl = codec.encode(url)
codec.decode(shortUrl)

# Algorithm to determine if a string has unique characters or not
def isunique( word ):
  if len(word) == len(set(word)):
    return True
  else:
    return False

word = "hello"

isunique(word)

# Do this without set!
# What if we didn't have sets?
char_list = []
def isunique( mystring ):
    for char in mystring:
        if char not in char_list:
            char_list.append(char)
        else:
            return False
    print ('True')

isunique('helo')


# BATTLESHIPS ON A BOARD MOTHERFUCKER!
# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's,
# empty slots are represented with '.'s. You may assume the following rules:
# 1. You'll receive a valid board with only empty slots or ships
# 2. Battleships can only be placed horizontally or vertically. In other words, they can only be made
# of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# 3. At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# Two battleships

# Count how many battle ships...
def ship_count(board):
    # The board is a list of lists apparently?
    counter = 0 # Keep track of stuff
    for i in range (len(board)): # For length of board (3) -- so this actually the ROWS
        for j in range (len(board[0])): # This is the number of columns, it's accessing the first entry in the list
            if board[i][j] == "X": # If the position we are at in our embedded list (row 1, column 1 then row 1 column 2, column 3) -- that is how this nesting works
                if i > 0 and board[i-1][j] == "X" or j > 0 and board[i][j-1] == "X": # If i is more than 0 and the thing behind i position j is an x or j is more than 0 and the thing behind
                    continue
                counter += 1 #Add one to the ship counter
    return counter

# Testcase
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
board
len(board)
len(board[0])
ship_count(board)

# Odd numbers
l = 27
r = 37

def oddNumbers(l, r):
    odds = []
    for item in list(range(l,r+1)): # REMEMBER RANGE IS WEIRD TO GET WHOLE THING ADD 1
        if item % 2 != 0:
            odds.append(item)
        else:
            continue
    return odds

# Friend groups
2%2
list(range(2,7))
