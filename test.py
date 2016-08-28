from main import Main


class Run(object):
    print("Neologism")
    def __init__(self):
        self.a=Main()
        self.a.launch()
        while self.a.du>0:
            self.a.index()
            self.a.choice()
        else:
            for letter in self.a.word:
                print letter,


b=Run()
