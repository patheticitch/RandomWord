import slate
import random


class Word(object):

    def __init__(self):

        with open('raven.pdf') as f:
            self.doc=slate.PDF(f)
            self.text=self.doc[random.randint(0,len(self.doc))]



















    #def make_string(self):
    #    self.text=self.doc[0]
        #return self.text
