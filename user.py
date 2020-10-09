import tkinter as tk
from tkinter import ttk


class UserView:
    def __init__(self):
        self.root = tk.Tk()
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
        self.root.geometry("+{}+{}".format(positionRight, positionDown))
        self.frame = tk.Frame(self.root).pack(anchor="c")
        msgLabel = ttk.Label(self.frame, text="Message")
        msgLabel.pack(side="left")

        scrollbar = ttk.Scrollbar(orient="horizontal")
        userEntry = tk.Entry(self.frame, font="Menlo", width=40)
        userEntry.focus()
        userEntry.pack(side="left")

        userEntry.bind("<Return>", self.send_input_user)

    def start(self):
        self.root.mainloop()

    def send_input_user(self, event):
        inputText = event.widget.get()
        name = User(inputText)
        self.root.destroy()
        MainChatView(name).start()


class User():
    def __init__(self, name):
        self.username = name


class MainChatView:

    def __init__(self, User):
        self.user = User.username
        self.root = tk.Tk()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.chatLog = tk.LabelFrame(self.root, bd=2, relief="groove")
        self.chatLog.pack(side="top", expand="yes",
                          padx=15, pady=15, fill="both")

        self.msgLog = tk.LabelFrame(self.chatLog, bd=0)
        self.msgLog.pack(side="left", expand="yes",
                         padx=5, fill="x", anchor="nw")

        self.bottomframe = tk.Frame(self.root, bd=0)
        self.bottomframe.pack(side="bottom", fill="x", padx=15, pady=15)

        text2 = tk.Label(self.msgLog, justify="left",
                         text=":Hey there mate! LoremLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem ",
                         anchor='nw')

        text2.pack(anchor="nw", fill="x", expand=True)

        text3 = tk.Label(self.msgLog, justify="left",
                         text="The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps. Bawds jog, flick quartz, vex nymphs. Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. Brick quiz whangs jumpy veldt fox. Bright vixens jump; dozy fowl quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sex-charged fop blew my ",
                         anchor='nw')

        text3.pack(anchor="nw", fill="x", expand=True)

        msgInput = tk.StringVar()
        msgLabel = ttk.Label(self.bottomframe, text="Message")
        msgLabel.pack(side="left")

        scrollbar = ttk.Scrollbar(orient="horizontal")
        self.msgEntry = tk.Entry(self.bottomframe, font="Menlo", textvariable=msgInput,
                                 width=30, xscrollcommand=scrollbar.set)
        self.msgEntry.focus()
        self.msgEntry.pack(side="left", fill="x", expand=True)

        text2.bind("<Configure>", self.set_label_wrap)
        text3.bind("<Configure>", self.set_label_wrap)
        self.msgEntry.bind("<Return>", self.send_input)

    def send_input(self, event):
        inputT = event.widget.get()
        if len(inputT) == 0 or inputT == " ":
            self.msgEntry.delete(0, 'end')
            return
        inputText = self.user + ":  " + event.widget.get()
        text2 = tk.Label(self.msgLog, justify="left",
                         text=inputText,
                         anchor='nw')
        text2.pack(fill="x", expand=True)
        text2.bind("<Configure>", self.set_label_wrap)
        self.msgEntry.delete(0, 'end')

    def set_label_wrap(self, event):
        wraplength = event.width - 1  # 12, to account for padding and borderwidth
        event.widget.configure(wraplength=wraplength)

    def start(self):
        self.root.mainloop()


UserView().start()
