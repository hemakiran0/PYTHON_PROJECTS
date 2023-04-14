import string
import tkinter as tk
import tkinter.messagebox
import random





colors = ['red','green','blue','yellow','purple','orange']
color = random.choice(colors)

code_length = 8
characters = string.ascii_letters+string.digits
access_code = ''.join(random.choice(characters) for i in range(code_length))

root=tk.Tk()

root.title('captche')
label = tk.Label(root, text = "creating capche").pack()
root.geometry('350x200')
l1 = tk.Label(root,text = access_code, bg =color).pack()

l2 = tk.Entry(root, bg='lightgray')
l2.pack()



def check():
    x = l2.get()
    if x == access_code:
        tk.messagebox.showinfo('result','access granted')
    else:
        tk.messagebox.showinfo('result', 'access denied')

l3 = tk.Button(root,text='submit',command=check).pack()

root.mainloop()