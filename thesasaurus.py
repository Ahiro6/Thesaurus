import json
import difflib
from tkinter import *

data = json.load(open("data.json", "r"))

window = Tk()
window.title("Thesasaurus")


def getDef(word):

    word = word.lower()

    if word in data:
        definition = data.get(word)
        return definition

    elif len(difflib.get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        word = difflib.get_close_matches(word, data.keys(), cutoff=0.8)[0]
        definition = data.get(word)
        definition.insert(0, "Did you mean " + word + "? \n")
        return definition

    elif word.upper() in data:
        definition = data.get(word.upper())
        return definition

    elif len(difflib.get_close_matches(word.upper(), data.keys(), cutoff=0.8)) > 0:
        word = difflib.get_close_matches(word.upper(), data.keys(), cutoff=0.8)[0]
        definition = data.get(word)
        return definition

    elif word.title() in data:
        definition = data.get(word.title())
        return definition

    elif len(difflib.get_close_matches(word.title(), data.keys(), cutoff=0.8)) > 0:
        word = difflib.get_close_matches(word.title(), data.keys(), cutoff=0.8)[0]
        definition = data.get(word)
        definition.insert(0, "Did you mean " + word + "? \n")
        return definition

    elif word == "":
        definition = "Please enter a word."
        return definition
    else:
        definition = "This word does not exist. Double check your entry."
        return definition


def update_window():
    word = e_value.get()
    definition = getDef(word)
    t.delete(0, END)
    id = 1
    print(definition)
    for i in definition:
        t.insert(END, str(id) + ". " + i)
        id += 1


b = Button(window, text="Enter", command=update_window, width=10)
b.grid(row=4, column=0, columnspan=2)
b_y = Button(window, text="Yes")
b_n = Button(window, text="No")

e_value = StringVar()
e = Entry(window, textvariable=e_value)
e.grid(row=1, column=1)

t = Listbox(window, width=40, height=10)
t.grid(row=2, column=1)

sc = Scrollbar(window, orient="horizontal")
sc.grid(row=3, column=0, columnspan=2)

sb = Scrollbar(window)
sb.grid(column=0, row=0, rowspan=4)

t.configure(xscrollcommand=sc.set)
sc.configure(command=t.xview)

t.configure(yscrollcommand=sb.set)
sb.configure(command=t.yview)

la = Label(window, text="Type a word:")
la.grid(row=0, column=0, columnspan=2)


window.mainloop()
