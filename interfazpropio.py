import tkinter as tk

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.label_user = tk.Label(master, text="Usuario:")
        self.label_user.pack()

        self.entry_user = tk.Entry(master)
        self.entry_user.pack()

        self.label_password = tk.Label(master, text="Contraseña:")
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        # Aquí se podría agregar la lógica de autenticación
        print("Usuario:", self.entry_user.get())
        print("Contraseña:", self.entry_password.get())

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Distripizza")

        self.button_login = tk.Button(master, text="Login", command=self.open_login_window)
        self.button_login.pack()

    def open_login_window(self):
        self.login_window = tk.Toplevel(self.master)
        LoginWindow(self.login_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

