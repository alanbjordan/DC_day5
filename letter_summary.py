#Letter Summary
#Write a letter_histogram program that asks the user for input, and 
#prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. 

word = input("Enter a word: ").lower()
d = {x:word.count(x) for x in word}
print(d)
