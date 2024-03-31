"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder():

    def __init__(self, path):
       dict_file = open(path)
       self.words = self.parse(dict_file)
       print (f"{len(self.words)} words read")

    # pass self to each method
    def parse(self, dict_file):
       return [w.strip() for w in dict_file]

    # pass self to each method
    def random(self):
       print (random.choice(self.words))
    

class SpecialWordFinder(WordFinder):
   
    # pass self to each method
    def parse(self, dict_file):

        return [word.strip() for word in dict_file 
            if word.strip() and not word.startswith("#")]
   



path = "words.txt"
wf = WordFinder(path)
wf.random()

path = "special_words.txt"
wf = SpecialWordFinder(path)