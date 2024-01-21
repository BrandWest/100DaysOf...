import pandas as pd
from random import randint
from os import path

class Cards():
    def __init__(self):
        super().__init__()
        self.word_list = self._saved_progress()
        self.word_dict = self.convert_to_dict()
        self.index = 0
        self.saved_progress = False
        
        

    def get_words(self):
        return pd.read_csv('/home/caboose/codingProjects/python/udemy/Day31 - Capstone - Falsh Cards/data/french_words.csv')
    

    def convert_to_dict(self):
        return self.word_list.to_dict()


    def random_word(self):
        self.index = randint(0, len(self.word_list)-1)
    

    def _saved_progress(self):
        if path.exists('/home/caboose/codingProjects/python/udemy/Day31 - Capstone - Falsh Cards/data/words_to_learn.csv'):
            self.saved_progress = True
            return pd.read_csv('/home/caboose/codingProjects/python/udemy/Day31 - Capstone - Falsh Cards/data/words_to_learn.csv')
            # self.word_dict = self.convert_to_dict()
            # self.index = randint(0, len(self.word_list)-1)
            # print("true")
        else:
            print("false")
            return self.get_words()