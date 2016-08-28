import random
from word import Word



class Main(object):
    a=Word()
    text=a.text


    def __init__(self):
        try:
            self.dic={1:"a",2:"b",3: "c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",
            17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"
            }
            #self.letter=[]
            self.word=[]
            self.l=len(self.text)
            self.du=int(raw_input("How long should your word be: "))-1
        except ValueError:
            print "Enter a number "
            self.__init__()





    def launch(self):
        self.ran=random.randint(1,26)
        self.first=self.dic.pop(self.ran)
        self.word.append(self.first)

    def index(self):
        self.letter=[]

        for index,char in enumerate(self.text): #runs trough the text
            if char.lower()==self.word[-1]: #checks for the last letter in word
                if index<(self.l-1):
                    #if it's not the last letter
                    if self.text[index+1]  in ',.:;!?' or self.text[index+1] == " ":
                        continue
                    else:

                        self.letter.append(self.text[index+1].lower())
                        
                     #appends all possibilities in letter[]
            else:
                continue



    def choice(self):
        try:
            self.word.append(random.choice(self.letter))
            self.du -= 1

        except IndexError:
            self.launch()#appends random word from choice to the word we want to create
        #del self.letter[:] #clears the letter list for new possibilities
