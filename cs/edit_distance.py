# From the cracking the code iterview book with problems
# Github they have all kinds of different problems
# Problem: there are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to
# check if they are one edit (or zero edits) away.

# EXAMPLE
# pale, ple —> true
# pales, pale —> true
# pale, bale —> true
# pale, bae —> false

# Count the number of changes for each one and then true if they are 1 or 0 and false if they are more than that!
# Edit distance!
# Naive Recursive version
def editDistance(s1, s2, m, n):
	if m==0:
		return n # Basically, if one of the strings is empty, edit distance will be the length of the other string (that many insertions)
	if n==0:
		return m # Same as above

	if str1[m-1] == str2[n-1]: # This is saying if the last letters in the string are the same, (yes it is last letter bc end index is always len-1)
		return editDistance(str1, str2, m-1, n-1) # call the function again on the remaining letters

	# It will keep doing this until it finds a difference, and THEN: return the minimum value
	return 1 + min(editDistance(str1, str2, m, n-1), # First check if there has been an insertion (m is 1 bigger than n)
	  			   editDistance(str1, str2, m-1, n), # A removal (m is 1 smaller than n)
				   editDistance(str1, str2, m-1, n-1)) # A replacement

	# The way this works is that each editDistance will go through, and each time you don't have a match, it will continue the loop --
	# For example if we compare fv vs. five, it will do the first one and see that we get 0 the first time, so add 1

str1 = "sunday"
str2 = "saturday"
print (editDistance(str1, str2, len(str1), len(str2)))


# dynamic programming version:
