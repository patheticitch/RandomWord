from main import Main


a=raw_input("Your name: ")
print("Portamteau")
def run(a):
    a=Main()
    a.launch()
    while a.du>0:
        a.index()
        a.choice()
    else:
        for letter in a.word:
            print letter,


run(a)
