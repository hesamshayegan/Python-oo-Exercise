"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """ find random words from a dictionary or a file """    
    def __init__(self, path):
        """ read dictionaries and reports and return # items read."""
               
        dict_file = open(path)
    
        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read in the file")
    
    def parse(self, dict_file):
        """ parse dict_file -> list of words"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """ return random word """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
     
    def parse(self, dict_file):
        """ parse dict_file -> list of words, exclude blanks and # """

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]



    
    
