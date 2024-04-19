import requests
import json
import os
from tkinter import *
import tkinter as tk
class Main(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.init_main()
    def init_main(self):
        toolbar = tk.Frame(bg="#d7d8e0", bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        id_label = Label(toolbar, text="id:", width=20)
        id_label.grid(row=1, column=1)
        id_num = Entry(toolbar, width=20)
        id_num.grid(row=1, column=2)

        createFile = Button(toolbar, text="download info with id", command=lambda: self.save(int(id_num.get())),background="#fcfcd5", width=40)
        createFile.grid(row=2, column=1, columnspan=2)
    def save(self,id):
        response = requests.get(f'https://jsonplaceholder.org/posts/{id}')
        y = json.loads(response.text)
        os.mkdir(f"file{id}")
        with open(f"file{id}/file{id}.txt", "w") as file:
            file.write(str(y))

if __name__ == "__main__":
    os.chdir(os.getcwd())
    window = tk.Tk()
    application = Main(window)
    application.pack()
    window.title("Дула на сегодня")
    window.mainloop()
