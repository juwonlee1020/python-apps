from tkinter import *

window = Tk()
def kg_convert():
    gram_text.delete("1.0", END)
    pound_text.delete("1.0", END)
    ounce_text.delete("1.0", END)

    kg = float(kg_var.get())
    gram = kg * 1000
    pound = kg * 2.20462
    ounce = kg * 35.274
    gram_text.insert(END, gram)
    pound_text.insert(END, pound)
    ounce_text.insert(END, ounce)
    return

kg_label = Label(window, text="kg")
kg_label.grid(row=0, column=0)

kg_var = StringVar()
kg_entry = Entry(window, textvariable=kg_var)
kg_entry.grid(row = 0, column = 1)

gram_text = Text(window, height=1, width=20)
gram_text.grid(row=1, column=0)

pound_text = Text(window, height=1, width=20)
pound_text.grid(row=1, column=1)

ounce_text = Text(window, height=1, width=20)
ounce_text.grid(row=1, column=2)

convert_button = Button(window, text="Convert", command = kg_convert)
convert_button.grid(row=0, column = 2)
window.mainloop()