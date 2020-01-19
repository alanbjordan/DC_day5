#Letter Summary
#Write a word_histogram program that asks the user for a sentence input, and 
#prints a dictionary containing the tally of how many times each word in the sentence was used. 

word = input("Enter a word: ").lower()
split_word = word.split(" ")
d = {
    x:word.count(x) for x in split_word
    }
print(d)