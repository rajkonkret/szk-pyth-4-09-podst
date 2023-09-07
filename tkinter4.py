import tkinter as tk

class GradeCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Grade Calculator")

        self.student_var = tk.StringVar(master)
        self.student_var.set("Uczeń 1")
        self.student_dropdown = tk.OptionMenu(master, self.student_var,
                                              'Uczeń 1', "Uczeń 2", "Uczeń 3")

        self.student_dropdown.pack()


root = tk.Tk()
calculator_app =GradeCalculator(root)
root.mainloop()