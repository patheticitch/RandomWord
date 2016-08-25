import random



class Main(object):
    text="This is a text message to try out if this script works or not. Good luck with that one"

    def __init__(self):
        self.dic={1:"a",2:"b",3: "c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",
        17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"
        }
        self.letter=[]
        self.word=[]
        self.l=len(self.text)
        self.text="This is a text message to try out if this script works or not. Good luck with that one, if the text is too short I will provide a loger one just for the fun."





        self.du=int(raw_input("How long should your word be: "))-1




    def launch(self):
        self.ran=random.randint(1,26)
        self.first=self.dic.pop(self.ran)
        self.word.append(self.first)

    def index(self):
        for index,char in enumerate(self.text): #runs trough the text
            if char.lower()==self.word[-1]: #checks for the last letter in word
                if index<(self.l-1):
                    #if it's not the last letter
                    #if char in ',.:;!?' and char != " ":
                        #continue
                    #else:
                self.letter.append(self.text[index+1].lower()) #appends all possibilities in letter[]
            else:
                continue



    def choice(self):
        try:
            self.word.append(random.choice(self.letter))
            self.du -= 1

        except IndexError:
            self.launch()#appends random word from choice to the word we want to create
        #del self.letter[:] #clears the letter list for new possibilities
