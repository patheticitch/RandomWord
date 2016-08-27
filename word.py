import slate


class Word(object):

    def __init__(self):
        with open('dawn.pdf') as f:
            self.doc=slate.PDF(f)
            self.text=self.doc[0]




    #def make_string(self):
    #    self.text=self.doc[0]
        #return self.text
