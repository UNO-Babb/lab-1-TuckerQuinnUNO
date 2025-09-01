#MadLib.py
#Name: Tucker Quinn
#Date: August 31st, 2025
#Assignment: Mad Lib 

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("Enter a plural noun: ")
adjective1 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
noun2 = input("Enter a plural noun: ")
adverb1 = input("Enter an adverb: ")
verb2 = input("Enter a verb: ")

  #Print the story with the user supplied words.

print("I love to eat " + noun1 + "!")
print("They taste so " + adjective1 + ".")
print("Sometimes I like to " + verb1 + " them.")
print("I also love to eat " + noun2 + ".")
print("I like to " + adverb1 + " devour them.")
print("But I can't " + verb2 + " them.")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
