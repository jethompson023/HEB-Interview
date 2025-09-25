import tkinter as tk
import time
from tkinter import font as tkfont

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1) 
        
        self.frames = {}
        
        for F in (StartPage, MainPage, Withdraw, Deposit, Balance):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="aqua")
        self.controller = controller
        self.controller.title("HEB ATM")
        self.controller.size="zoomed"
        self.controller.iconphoto(False, tk.PhotoImage(file='atm.png'))
        
        h1 = tk.Label(self, text="Welcome to HEB ATM", font=('Helvetica', 45, 'bold'), bg="blue", fg="white")
        
        h1.pack(side="top", fill="x", pady=25)
        
        space_label = tk.Label(self, height = 4, bg="aqua")
        space_label.pack()
        
        
        #start page for the ATM
        pin_label = tk.Label(self, text="Please enter your PIN:", font=('Helvetica', 14), bg="aqua", fg="black")
        pin_label.pack(pady=10)
        
        #pin for the user to enter
        my_pin = tk.StringVar()
        pin_entry = tk.Entry(self, textvariable=my_pin, font=('Helvetica', 14), width=20, show="*")
        pin_entry.focus()
        pin_entry.pack()
        
        pin_entry.bind('<Return>', lambda event: enter_button.invoke())
        
        def check_pin():
            pin = my_pin.get()
            if pin == '1234':
                controller.show_frame("MainPage")
            else:
                error_label.config(text="Invalid PIN. Please try again.")
        
        enter_button = tk.Button(self, text="Enter", font=('Helvetica', 14), command=check_pin)
        enter_button.pack(pady=20)
        
        incorrect_pin = tk.Label(self, text="", font=('Helvetica', 12), fg="red", bg="aqua")
        incorrect_pin.pack()
        error_label = incorrect_pin
        
        bottom_frame = tk.Frame(self, bg="white", borderwidth=20)
        bottom_frame.pack(side="bottom", fill="x", pady=20)
        
        def tick():
            current_time = time.strftime('%I:%M %p')
            clock_label.config(text=current_time)
            clock_label.after(200, tick)
            
        clock_label = tk.Label(bottom_frame, font=('Helvetica', 14), bg="white")
        clock_label.pack(side="right")
        tick()
        
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="lightblue")
        self.controller = controller
        
        main_label = tk.Label(self, text="Main Menu", font=controller.title_font)
        main_label.pack(side="top", fill="x", pady=10)
        
        bottom_frame = tk.Frame(self, bg="white", borderwidth=20)
        bottom_frame.pack(side="bottom", fill="x", pady=20)
        
        def tick():
            current_time = time.strftime('%I:%M %p')
            clock_label.config(text=current_time)
            clock_label.after(200, tick)
            
        clock_label = tk.Label(bottom_frame, font=('Helvetica', 14), bg="white")
        clock_label.pack(side="right")
        tick()
        
        main_menu_label = tk.Label(self, text="Select an option:", font=('Helvetica', 14), bg="lightblue", anchor="w")
        main_menu_label.pack(pady=20)
        
        button_frame = tk.Frame(self, bg="green")
        button_frame.pack(fill="both", expand=True)
        
        def withdraw():
            controller.show_frame("Withdraw")
        
        withdraw_button = tk.Button(button_frame, text="Withdraw", command=withdraw, relief="raised", borderwidth=3, width=50, height=5)
        withdraw_button.grid(row=0, column=0, pady=5)
        
        def deposit():
            controller.show_frame("Deposit")
            
        deposit_button = tk.Button(button_frame, text="Deposit", command=deposit, relief="raised", borderwidth=3, width=50, height=5)
        deposit_button.grid(row=1, column=0, pady=5)
        
        def balence():
            controller.show_frame("Balance")
        
        balence_button = tk.Button(button_frame, text="Balence", command=balence, relief="raised", borderwidth=3, width=50, height=5)
        balence_button.grid(row=2, column=0, pady=5)
       

        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
class Withdraw(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="green")
        self.controller = controller
        
        label = tk.Label(self, text="Withdraw", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        choose_amount_label = tk.Label(self, text="Choose an amount to withdraw:", font=('Helvetica', 14), bg="green", fg="black")
        choose_amount_label.pack(pady=20)
        
        button_frame = tk.Frame(self, bg="lightgreen")
        button_frame.pack(fill="both", expand=True)
        
        twenty_button = tk.Button(button_frame, text="$20", relief="raised", borderwidth=3, width=20, height=5)
        twenty_button.grid(row=0, column=0, pady=5, padx=10)
        
        forty_button = tk.Button(button_frame, text="$40", relief="raised", borderwidth=3, width=20, height=5)
        forty_button.grid(row=1, column=0, pady=5, padx=10)
        
        sixty_button = tk.Button(button_frame, text="$60", relief="raised", borderwidth=3, width=20, height=5)
        sixty_button.grid(row=2, column=0, pady=5, padx=10)
        
        eighty_button = tk.Button(button_frame, text="$80", relief="raised", borderwidth=3, width=20, height=5)
        eighty_button.grid(row=3, column=0, pady=5, padx=10)
        
        hundred_button = tk.Button(button_frame, text="$100", relief="raised", borderwidth=3, width=20, height=5)
        hundred_button.grid(row=0, column=1, pady=5, padx=10)
        
        hundred_twenty_button = tk.Button(button_frame, text="$120", relief="raised", borderwidth=3, width=20, height=5)
        hundred_twenty_button.grid(row=1, column=1, pady=5, padx=10)
        
        hundred_fifty_button = tk.Button(button_frame, text="$150", relief="raised", borderwidth=3, width=20, height=5)
        hundred_fifty_button.grid(row=2, column=1, pady=5, padx=10)
        
        hundred_eighty_button = tk.Button(button_frame, text="$180", relief="raised", borderwidth=3, width=20, height=5)
        hundred_eighty_button.grid(row=2, column=1, pady=5, padx=10)
        
        
        cash = tk.StringVar()
        other_entry = tk.Entry(button_frame, textvariable=cash, font=('Helvetica', 14), width=59, justify="right")
        other_entry.grid(row=3, column=1, pady=5, ipady=30)
        other_entry.insert(0, "Other Amount")
        
        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            cash.set('')
            controller.show_frame("MenuPage")
        other_entry.bind('<Return>', other_amount)
        
        bottom_frame = tk.Frame(self, bg="white", borderwidth=20)
        bottom_frame.pack(side="bottom", fill="x", pady=20)
        
        def tick():
            current_time = time.strftime('%I:%M %p')
            clock_label.config(text=current_time)
            clock_label.after(200, tick)
            
        clock_label = tk.Label(bottom_frame, font=('Helvetica', 14), bg="white")
        clock_label.pack(side="right")
        tick()
        
        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Deposit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="orange")
        self.controller = controller
        label = tk.Label(self, text="Deposit", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        bottom_frame = tk.Frame(self, bg="white", borderwidth=20)
        bottom_frame.pack(side="bottom", fill="x", pady=20)
        
        def tick():
            current_time = time.strftime('%I:%M %p')
            clock_label.config(text=current_time)
            clock_label.after(200, tick)
            
        clock_label = tk.Label(bottom_frame, font=('Helvetica', 14), bg="white")
        clock_label.pack(side="right")
        tick()
        
        button = tk.Button(self, text="Logout",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Balance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="purple")
        self.controller = controller
        label = tk.Label(self, text="Balence", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        bottom_frame = tk.Frame(self, bg="white", borderwidth=20)
        bottom_frame.pack(side="bottom", fill="x", pady=20)
        
        def tick():
            current_time = time.strftime('%I:%M %p')
            clock_label.config(text=current_time)
            clock_label.after(200, tick)
            
        clock_label = tk.Label(bottom_frame, font=('Helvetica', 14), bg="white")
        clock_label.pack(side="right")
        tick()
        
        button = tk.Button(self, text="Go to Start Page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()