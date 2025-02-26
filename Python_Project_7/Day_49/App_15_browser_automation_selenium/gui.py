import tkinter as tk
from tkinter import ttk
from main import WebAutomation
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Browser Automation")

        # Create widgets
        # Login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username:").grid(
            row=0, column=0, sticky="w"
        )
        self.enter_username = tk.Entry(self.login_frame)
        self.enter_username.grid(row=0, column=1, sticky="ew")

        tk.Label(self.login_frame, text="Password:").grid(
            row=1, column=0, sticky="w"
        )
        self.enter_password = tk.Entry(self.login_frame)
        self.enter_password.grid(row=1, column=1, sticky="ew")

        # Form email submission frame
        self.email_frame = tk.Frame(self.root)
        self.email_frame.pack(padx=10, pady=10)

        tk.Label(self.email_frame, text="Email:").grid(
            row=0, column=0, sticky="w"
        )
        self.enter_email = tk.Entry(self.email_frame)
        self.enter_email.grid(row=0, column=1, sticky="ew")

        tk.Label(self.email_frame, text="Language:").grid(
            row=1, column=0, sticky="w"
        )
        self.language_options = ["JavaScript", "Python", "Java", "C++", "Ruby"]
        self.language_combobox = ttk.Combobox(
            self.email_frame, values=self.language_options
        )
        self.language_combobox.grid(row=1, column=1, sticky="ew")

        # Buttons
        self.button_frame = tk.Frame()
        self.button_frame.pack(padx=10, pady=10)

        tk.Button(
            self.button_frame, text="Submit", command=self.submit_data
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            self.button_frame, text="Close Browser", command=self.close_browser
        ).grid(row=0, column=1, padx=5)

    def submit_data(self):
        username = self.enter_username.get()
        password = self.enter_password.get()
        email = self.enter_email.get()
        language = self.language_combobox.get()

        self.web_automation = WebAutomation()
        self.web_automation.Login(username, password)
        self.web_automation.OpenSecondWebpage()
        self.web_automation.fill_out_email_form(email, language)

        print(f"Username: {username}, Password: {password}, "
              f"Email: {email}, Language: {language}")

    def close_browser(self):
        self.web_automation.close_browser()
        messagebox.showinfo("Submitted Data Successfully", "Browser Closed")


root = tk.Tk()
app = App(root)
root.mainloop()
